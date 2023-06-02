from io import BytesIO
from typing import Optional, Union, List

from aiohttp import ClientSession
from PIL import Image, ImageDraw, ImageFont, ImageColor
from .error import InvalidImageUrl
from pathlib import Path
from .card_settings import Settings

class Sandbox:
    """class to create your own cards

    Parameters
    ----------
    settings: :class:`Settings`
        The settings for the rank card

    cacheing: :class:`bool`
        Whether to cache the image or not. Default is `True`

    avatar: :class:`Union[PathLike, BufferedIOBase]`
        The avatar image for the rank card. This can be a path to a file or a file-like object in `rb` mode
    
    level: :class:`int`
        The level of the member
    
    username: :class:`str`
        The username of the member
    
    current_exp: :class:`int`
        The current amount of XP the member has
    
    max_exp: :class:`int`
        The amount of XP required for the member to level up
    
    rank: Optional[:class:`int`]
        The rank of the member. Default is `None`

    Attributes
    ----------
    - `settings`
    - `cacheing`
    - `avatar`
    - `level`
    - `username`
    - `current_exp`
    - `max_exp`
    - `rank`

    Methods
    -------
    - `custom_card1`
        Creates a rank card with the first design
    -  `custom_canvas`
        A blank canvas to make whatever you want!

    Raises
    ------
    - `InvalidImageType`
        If the image type is not supported
    - `InvalidImageUrl`
        If the image url is invalid

    """

    __slots__ = ('background', 'cacheing', 'rank', 'background_color', 'text_color', 'bar_color', 'settings', 'avatar', 'level', 'username', 'current_exp', 'max_exp')

    def __init__(
        self,
        settings: Settings,
        avatar: str,
        level:int,
        username:str,
        current_exp:int,
        max_exp:int,
        cacheing:bool = True,
        rank:Optional[int] = None

    ):
        self.background = settings.background
        self.background_color = settings.background_color
        self.avatar = avatar
        self.level = level
        self.rank = rank
        self.username = username
        self.current_exp = current_exp
        self.max_exp = max_exp
        self.bar_color = settings.bar_color
        self.text_color = settings.text_color
        self.cacheing = cacheing

    @staticmethod
    def _convert_number(number: int) -> str:
        if number >= 1000000000:
            return f"{number / 1000000000:.1f}B"
        elif number >= 1000000:
            return f"{number / 1000000:.1f}M"
        elif number >= 1000:
            return f"{number / 1000:.1f}K"
        else:
            return str(number)

    @staticmethod
    async def _image(url:str):
        async with ClientSession()   as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise InvalidImageUrl(f"Invalid image url: {url}")
                data = await response.read()
                return Image.open(BytesIO(data))

    async def custom_card1(
            self,
            card_colour: str = "black",
            resize: int = 100
        )-> Union[None, bytes]:
        """
        Sandbox for first type of card and returns `bytes`

        Parameters
        ----------
        card_colour: :class:`str`
            The color of the card. Default is `black`, you can use hex color codes with '#' too
        
        resize: :class:`int`
            The size of the avatar. Default is `100`

        Attributes
        ----------
        - `card_colour`
        - `resize`

        """
        path = str(Path(__file__).parent)

        if isinstance(self.avatar, str):
            if self.avatar.startswith("http"):
                self.avatar = await Sandbox._image(self.avatar)
        elif isinstance(self.avatar, Image.Image):
            pass
        else:
            raise TypeError(f"avatar must be a url, not {type(self.avatar)}") 

        self.avatar = self.avatar.resize((170,170))

        if card_colour == "black":
            overlay = Image.open(path + "/assets/overlay1.png")
        elif Path(path + f"/assets/{card_colour.replace('#','')}_overlay1.png").is_file():
            overlay = Image.open(path + f"/assets/{card_colour.replace('#','')}_overlay1.png")
        else:
            overlay = Image.open(path + "/assets/overlay1.png")
            bg = overlay.convert("RGBA")
            data = bg.load()

            for x in range(bg.size[0]):
                for y in range(bg.size[1]):
                    if data[x,y] == (0,0,0,255):
                        data[x,y] = ImageColor.getcolor(card_colour, "RGBA")
            if self.cacheing:
                bg.save(path + f"/assets/{card_colour.replace('#','')}_overlay1.png", 'PNG')
            
            overlay = bg
        
        background = Image.new("RGBA", overlay.size)
        backgroundover = self.background.resize((638,159))
        background.paste(backgroundover,(0,0))
        
        self.background = background.resize(overlay.size)
        self.background.paste(overlay,(0,0),overlay)

        myFont = ImageFont.truetype(path + "/assets/levelfont.otf",40)
        draw = ImageDraw.Draw(self.background)

        draw.text((205,(327/2)+20), self.username,font=myFont, fill=self.text_color,stroke_width=1,stroke_fill=(0, 0, 0))
        bar_exp = (self.current_exp/self.max_exp)*420
        if bar_exp <= 50:
            bar_exp = 50    

        current_exp = Sandbox._convert_number(self.current_exp)
        
        max_exp = Sandbox._convert_number(self.max_exp)
        
        myFont = ImageFont.truetype(path + "/assets/levelfont.otf",30)
        draw.text((197,(327/2)+125), f"LEVEL - {Sandbox._convert_number(self.level)}",font=myFont, fill=self.text_color,stroke_width=1,stroke_fill=(0, 0, 0))

        w,_ = draw.textsize(f"{current_exp}/{max_exp}", font=myFont)
        draw.text((638-w-50,(327/2)+125), f"{current_exp}/{max_exp}",font=myFont, fill=self.text_color,stroke_width=1,stroke_fill=(0, 0, 0))

        mask_im = Image.open(path + "/assets/mask_circle.jpg").convert('L').resize((170,170))
        new = Image.new("RGB", self.avatar.size, (0, 0, 0))
        try:
            new.paste(self.avatar, mask=self.avatar.convert("RGBA").split()[3])
        except Exception as e:
            print(e)
            new.paste(self.avatar, (0,0))
        self.background.paste(new, (13, 65), mask_im)

        im = Image.new("RGB", (490, 51), ImageColor.getcolor(card_colour, "RGB"))
        draw = ImageDraw.Draw(im, "RGBA")
        draw.rounded_rectangle((0, 0, 420, 50), 30, fill=(255,255,255,50))
        if self.current_exp != 0:
            draw.rounded_rectangle((0, 0, bar_exp, 50), 30, fill=self.bar_color)
        self.background.paste(im, (190, 235))
        new = Image.new("RGBA", self.background.size)
        new.paste(self.background,(0, 0), Image.open(path + "/assets/curvedoverlay.png").convert("L"))
        self.background = new.resize((505, 259))

        image = BytesIO()
        if resize != 100:
            self.background = self.background.resize((int(self.background.size[0]*(resize/100)), int(self.background.size[1]*(resize/100))))
        
        self.background.save(image, 'PNG')
        image.seek(0)
        return image


    async def custom_canvas(
            self,

            has_background: bool = True,
            background_colour: str = "black",

            canvas_size: tuple = (1000, 333),

            resize:int = 100,

            overlay: Union[None, List] = [[(1000-50, 333-50),(25, 25), "black", 200]],
            
            avatar_frame: str = "curvedborder",
            avatar_size: int = 260,
            avatar_position: tuple = (53, 36),
            
            text_font: str = "levelfont.otf",

            username_position: tuple = (330,130),
            username_font_size: int = 50,

            level_position: tuple = (500,40),
            level_font_size: int = 50,

            exp_position: tuple = (775,130),
            exp_font_size: int = 50,
            bar_exp: Union[None, int] = None,

            exp_bar_width: int = 619,
            exp_bar_height: int = 50,
            exp_bar_background_colour: Union[str, tuple] = "white",
            exp_bar_position:tuple = (330, 235),
            exp_bar_curve: int = 30,
            extra_text: Union[List, None] = None


        )-> Union[None, bytes]:
        """
        Sandbox for third type of card which returns "BytesIO"

        Parameters
        ----------
        has_background: :class:`bool`
            Whether to use a background image or not. Default is True
        
        background_colour: :class:`str`
            The colour of the background, only used if has_background is set to False. Default is black.
        
        canvas_size: :class:`tuple`
            The size of the canvas. Default is (1000, 333)
        
        resize: :class:`int`
            The percentage to resize the image to. Default is 100
                    
        overlay: :class:`list`
            A list of overlays to be placed on the background. Default is [[(1000-50, 333-50),(25, 25), "black", 200]].

        avatar_frame: :class:`str`
            `circle` `square` `curvedborder` `hexagon` or path to a self created mask.
        
        text_font: :class:`str`
            Default is `levelfont.otf` or path to a custom otf or ttf file type font.

        avatar_size: :class:`int`
            size of the avatar. Default is 260.

        avatar_position: :class:`tuple`
            pixel position of the avatar to be placed at. Default is (53, 36)

        username_position: :class:`tuple`
            pixel position of the username to be placed at. Default is (330,130)
        
        username_font_size: :class:`int`
            font size of the username. Default is 50.
        
        level_position: :class:`tuple`
            pixel position of the level to be placed at. Default is (500,40)
        
        level_font_size: :class:`int`
            font size of the level. Default is 50.

        exp_position: :class:`tuple`
            pixel position of the exp to be placed at. Default is (775,130)
        
        exp_font_size: :class:`int`
            font size of the exp. Default is 50.

        exp_bar_width: :class:`int`
            width of the exp bar. Default is 619.
        
        exp_bar_height: :class:`int`
            height of the exp bar. Default is 50.
        
        exp_bar_background_colour: :class:`str`
            colour of the exp bar. Default is white.
        
        exp_bar_position: :class:`tuple`
            pixel position of the exp bar to be placed at. Default is (330, 235)
        
        exp_bar_curve: :class:`int`
            curve of the exp bar. Default is 30.

        extra_text: :class:`list`
            list of tuples containing text and position of the text to be placed on the card. Default is None. eg ["string", (x-position, y-position), font-size, "colour"]

        exp_bar: :class:`int`
            The calculated exp of the user. Default is None.
        

        Attributes
        ----------
        - `has_background`
        - `background_colour`
        - `canvas_size`
        - `resize`
        - `overlay`
        - `avatar_frame`
        - `text_font`
        - `avatar_size`
        - `avatar_position`
        - `username_position`
        - `username_font_size`
        - `level_position`
        - `level_font_size`
        - `exp_position`
        - `exp_font_size`
        - `exp_bar_width`
        - `exp_bar_height`
        - `exp_bar_background_colour`
        - `exp_bar_position`
        - `exp_bar_curve`
        - `extra_text`
        - `exp_bar`
        
        """
        path = str(Path(__file__).parent)

        if isinstance(self.avatar, str):
            if self.avatar.startswith("http"):
                self.avatar = await Sandbox._image(self.avatar)
        elif isinstance(self.avatar, Image.Image):
            pass
        else:
            raise TypeError(f"avatar must be a url, not {type(self.avatar)}") 

        if has_background:
            background = self.background.resize(canvas_size)
        else:
            background = Image.new("RGBA", canvas_size, ImageColor.getcolor(background_colour, "RGB"))
        if overlay is not None:
            for x in overlay:
                cut = Image.new("RGBA", x[0] , ImageColor.getcolor(x[2], "RGB")+(x[3],))
                background.paste(cut, x[1] ,cut)

        avatar = self.avatar.resize((avatar_size, avatar_size))

        if avatar_frame == "square":
            mask = Image.new("RGBA", (avatar_size, avatar_size), "white")
        elif avatar_frame == "circle":
            mask = Image.open(path + "/assets/mask_circle.jpg").resize((avatar_size, avatar_size))
        elif avatar_frame == "hexagon":
            mask = Image.open(path + "/assets/mask_hexagon.png").resize((avatar_size, avatar_size))
        else:
            try:
                mask = Image.open(avatar_frame).resize((avatar_size, avatar_size))
            except:
                mask = Image.open(path + "/assets/curveborder.png").resize((avatar_size, avatar_size))

        new = Image.new("RGBA", avatar.size, (0, 0, 0))
        try:
            new.paste(avatar, mask=avatar.convert("RGBA").split()[3])
        except:
            new.paste(avatar, (0,0))
        
        background.paste(new, avatar_position, mask.convert("L"))

        if text_font == "levelfont.otf":
            fontname = path + "/assets/levelfont.otf"
        else:
            try:
                fontname = text_font
            except:
                fontname = path + "/assets/levelfont.otf"

        draw = ImageDraw.Draw(background)

        if self.rank is not None:
            combined = "LEVEL: " + self._convert_number(self.level) + "       " + "RANK: " + str(self.rank)
        else:
            combined = "LEVEL: " + self._convert_number(self.level)
        draw.text(level_position, combined,font=ImageFont.truetype(fontname,level_font_size), fill=self.text_color,stroke_width=1,stroke_fill=(0, 0, 0))
        draw.text(username_position, self.username,font=ImageFont.truetype(fontname,username_font_size), fill=self.text_color,stroke_width=1,stroke_fill=(0, 0, 0))

        if extra_text is not None and type(extra_text) == list:
            for x in extra_text:
                draw.text(x[1], x[0],font=ImageFont.truetype(fontname,x[2]), fill=(ImageColor.getcolor(x[3], "RGBA") if type(x[3]) != tuple else extra_text),stroke_width=1,stroke_fill=(0, 0, 0))

        exp = f"{self._convert_number(self.current_exp)}/{self._convert_number(self.max_exp)}"
        draw.text(exp_position, exp,font=ImageFont.truetype(fontname,exp_font_size), fill=self.text_color,stroke_width=1,stroke_fill=(0, 0, 0))

        if bar_exp == None:
            bar_exp = (self.current_exp/self.max_exp)*exp_bar_width
            exp_bar_curve_custom = exp_bar_curve
        else:
            bar_exp = bar_exp*exp_bar_width

        if bar_exp <= 50:
            bar_exp = 50
            exp_bar_curve_custom = exp_bar_curve//2

        im = Image.new("RGBA", (exp_bar_width+1, exp_bar_height+1))
        draw = ImageDraw.Draw(im, "RGBA")
        draw.rounded_rectangle((0, 0, exp_bar_width, exp_bar_height), exp_bar_curve, fill=(exp_bar_background_colour if type(exp_bar_background_colour) == tuple else ImageColor.getcolor(exp_bar_background_colour, "RGBA")))
        if self.current_exp != 0:
            draw.rounded_rectangle((0, 0, bar_exp, exp_bar_height), exp_bar_curve_custom, fill=self.bar_color)

        background.paste(im, exp_bar_position, im.convert("RGBA"))

        image = BytesIO()
        if resize != 100:
            background = background.resize((int(background.size[0]*(resize/100)), int(background.size[1]*(resize/100))))
        background.save(image, 'PNG')
        image.seek(0)
        return image