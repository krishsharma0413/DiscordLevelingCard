from io import BytesIO
from typing import Optional, Union

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



