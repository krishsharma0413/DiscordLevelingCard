from io import BytesIO
from typing import Optional, Union

from aiohttp import ClientSession
from PIL import Image, ImageDraw, ImageFont
from .error import InvalidImageUrl
from pathlib import Path
from .card_settings import Settings

class RankCard:
    """Class for creating a rank cards

    Parameters
    ----------
    settings: :class:`Settings`
        The settings for the rank card

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
    - `avatar`
    - `level`
    - `username`
    - `current_exp`
    - `max_exp`
    - `rank`

    Methods
    -------
    - `card1`
        Creates a rank card with the first design
    - `card2`
        Creates a rank card with the second design
    - `card3`
        Creates a rank card with the third design

    Raises
    ------
    - `InvalidImageType`
        If the image type is not supported
    - `InvalidImageUrl`
        If the image url is invalid

    """

    __slots__ = ('background', 'rank', 'background_color', 'text_color', 'bar_color', 'settings', 'avatar', 'level', 'username', 'current_exp', 'max_exp')



    def __init__(
        self,
        settings: Settings,
        avatar: str,
        level:int,
        username:str,
        current_exp:int,
        max_exp:int,
        rank:Optional[int] = None
    )-> None:
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


    async def card1(self, resize: int = 100)-> Union[None, bytes]:
        """
        Creates the rank card and returns `bytes`

        Parameters
        ----------
        resize: :class:`int`
            The percentage to resize the image to. Default is 100

        Attributes
        ----------
        - `resize`
        
        ![card](https://user-images.githubusercontent.com/77439837/234198272-3dcaabb0-0f38-4d51-9938-de4b0ad42123.png)
        """
        path = str(Path(__file__).parent)

        if isinstance(self.avatar, str):
            if self.avatar.startswith("http"):
                self.avatar = await RankCard._image(self.avatar)
        elif isinstance(self.avatar, Image.Image):
            pass
        else:
            raise TypeError(f"avatar must be a url, not {type(self.avatar)}") 

        self.avatar = self.avatar.resize((170,170))

        overlay = Image.open(path + "/assets/overlay1.png")
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

        current_exp = RankCard._convert_number(self.current_exp)
        
        max_exp = RankCard._convert_number(self.max_exp)
        
        myFont = ImageFont.truetype(path + "/assets/levelfont.otf",30)
        draw.text((197,(327/2)+125), f"LEVEL - {RankCard._convert_number(self.level)}",font=myFont, fill=self.text_color,stroke_width=1,stroke_fill=(0, 0, 0))

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

        im = Image.new("RGB", (490, 51), (0, 0, 0))
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


    async def card2(self, resize: int = 100)-> Union[None, bytes]:
        """
        Creates the rank card and returns `bytes`

        Parameters
        ----------
        resize: :class:`int`
            The percentage to resize the image to. Default is 100

        Attributes
        ----------
        - `resize`
        
        ![card](https://user-images.githubusercontent.com/77439837/234198354-315e9420-9bd7-47bd-87ed-b21c3772646c.png)
        """
        path = str(Path(__file__).parent)

        if isinstance(self.avatar, str):
            if self.avatar.startswith("http"):
                self.avatar = await RankCard._image(self.avatar)
        elif isinstance(self.avatar, Image.Image):
            pass
        else:
            raise TypeError(f"avatar must be a url, not {type(self.avatar)}") 

        background = Image.new("RGB", (1000, 333), self.background_color)
        background.paste(Image.new("RGB", (950, 333-50), "#2f3136"), (25, 25) )

        avatar = self.avatar.resize((260, 260))

        mask = Image.open(path + "/assets/curveborder.png").resize((260, 260))

        new = Image.new("RGBA", avatar.size, (0, 0, 0))
        try:
            new.paste(avatar, mask=avatar.convert("RGBA").split()[3])
        except:
            new.paste(avatar, (0,0))
        
        background.paste(new, (53, 73//2), mask.convert("L"))

        myFont = ImageFont.truetype(path + "/assets/levelfont.otf",50)
        draw = ImageDraw.Draw(background)

        if self.rank is not None:
            combined = "LEVEL: " + self._convert_number(self.level) + "       " + "RANK: " + str(self.rank)
        else:
            combined = "LEVEL: " + self._convert_number(self.level)
        w = draw.textlength(combined, font=myFont)
        draw.text((950-w,40), combined,font=myFont, fill=self.text_color,stroke_width=1,stroke_fill=(0, 0, 0))
        draw.text((330,130), self.username,font=myFont, fill=self.text_color,stroke_width=1,stroke_fill=(0, 0, 0))

        exp = f"{self._convert_number(self.current_exp)}/{self._convert_number(self.max_exp)}"
        w = draw.textlength(exp, font=myFont)
        draw.text((950-w,130), exp,font=myFont, fill=self.text_color,stroke_width=1,stroke_fill=(0, 0, 0))

        bar_exp = (self.current_exp/self.max_exp)*619
        if bar_exp <= 50:
            bar_exp = 50  

        im = Image.new("RGB", (620, 51), "#2f3136")
        draw = ImageDraw.Draw(im, "RGBA")
        draw.rounded_rectangle((0, 0, 619, 50), 30, fill=(255,255,255,50))
        
        if self.current_exp != 0:
            draw.rounded_rectangle((0, 0, bar_exp, 50), 30, fill=self.bar_color)
        
        background.paste(im, (330, 235))

        image = BytesIO()
        if resize != 100:
            background = background.resize((int(background.size[0]*(resize/100)), int(background.size[1]*(resize/100))))
        background.save(image, 'PNG')
        image.seek(0)
        return image

    async def card3(self, resize: int = 100)-> Union[None, bytes]:
        """
        Creates the rank card and returns `bytes`

        Parameters
        ----------
        resize: :class:`int`
            The percentage to resize the image to. Default is 100

        Attributes
        ----------
        - `resize`
        
        ![card](https://user-images.githubusercontent.com/77439837/234203410-a6a970ef-c01c-454b-be67-6dc7c1b2c807.png)
        """
        path = str(Path(__file__).parent)

        if isinstance(self.avatar, str):
            if self.avatar.startswith("http"):
                self.avatar = await RankCard._image(self.avatar)
        elif isinstance(self.avatar, Image.Image):
            pass
        else:
            raise TypeError(f"avatar must be a url, not {type(self.avatar)}") 

        background = self.background.resize((1000, 333))
        cut = Image.new("RGBA", (950, 333-50) , (0, 0, 0, 200))
        background.paste(cut, (25, 25) ,cut)

        avatar = self.avatar.resize((260, 260))

        mask = Image.open(path + "/assets/curveborder.png").resize((260, 260))

        new = Image.new("RGBA", avatar.size, (0, 0, 0))
        try:
            new.paste(avatar, mask=avatar.convert("RGBA").split()[3])
        except:
            new.paste(avatar, (0,0))
        
        background.paste(new, (53, 73//2), mask.convert("L"))
        myFont = ImageFont.truetype(path + "/assets/levelfont.otf",50)
        draw = ImageDraw.Draw(background)

        if self.rank is not None:
            combined = "LEVEL: " + self._convert_number(self.level) + "       " + "RANK: " + str(self.rank)
        else:
            combined = "LEVEL: " + self._convert_number(self.level)
        w = draw.textlength(combined, font=myFont)
        draw.text((950-w,40), combined,font=myFont, fill=self.text_color,stroke_width=1,stroke_fill=(0, 0, 0))
        draw.text((330,130), self.username,font=myFont, fill=self.text_color,stroke_width=1,stroke_fill=(0, 0, 0))

        exp = f"{self._convert_number(self.current_exp)}/{self._convert_number(self.max_exp)}"
        w = draw.textlength(exp, font=myFont)
        draw.text((950-w,130), exp,font=myFont, fill=self.text_color,stroke_width=1,stroke_fill=(0, 0, 0))

        bar_exp = (self.current_exp/self.max_exp)*619
        if bar_exp <= 50:
            bar_exp = 50  

        im = Image.new("RGBA", (620, 51))
        draw = ImageDraw.Draw(im, "RGBA")
        draw.rounded_rectangle((0, 0, 619, 50), 30, fill=(255,255,255,225))
        if self.current_exp != 0:
            draw.rounded_rectangle((0, 0, bar_exp, 50), 30, fill=self.bar_color)
        
        background.paste(im, (330, 235), im.convert("RGBA"))

        image = BytesIO()
        if resize != 100:
            background = background.resize((int(background.size[0]*(resize/100)), int(background.size[1]*(resize/100))))
        background.save(image, 'PNG')
        image.seek(0)
        return image