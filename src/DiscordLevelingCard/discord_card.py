from aiohttp import ClientSession
from PIL import Image, ImageDraw, ImageFont
from os import PathLike
from io import BufferedIOBase, IOBase, BytesIO
from typing import Union


class CardMaker:

    def convert_number(self, number: int) -> str:
        if number >= 1000000000:
            return f"{number / 1000000000:.1f}B"
        elif number >= 1000000:
            return f"{number / 1000000:.1f}M"
        elif number >= 1000:
            return f"{number / 1000:.1f}K"
        else:
            return str(number)


    async def image_(self, url:str):
        async with ClientSession() as session:
            async with session.get(url) as response:
                data = await response.read()
                return Image.open(BytesIO(data))

    async def type1(
        self,
        background: Union[PathLike, BufferedIOBase],
        avatar: Union[PathLike, BufferedIOBase],
        level:int,
        username:str,
        current_exp:int,
        max_exp:int,
        bar_color:str="white",
        text_color:str="white",
        path:str=None
    )-> Union[None, bytes]:
        if isinstance(background, IOBase):
            if not (background.seekable() and background.readable() and background.mode == "rb"):
                raise ValueError(f"File buffer {background!r} must be seekable and readable and in binary mode")
            self.background = Image.open(background)
        elif isinstance(background, str):
            if background.startswith("http"):
                self.background = await self.image_(background)
            else:
                self.background = Image.open(open(background, "rb"))
        else:
            raise TypeError(f"background must be a path or a file buffer, not {type(background)}") 


        if isinstance(avatar, IOBase):
            if not (avatar.seekable() and avatar.readable() and avatar.mode == "rb"):
                raise ValueError(f"File buffer {avatar!r} must be seekable and readable and in binary mode")
            self.avatar = Image.open(avatar)
        elif isinstance(avatar, str):
            if avatar.startswith("http"):
                self.avatar = await self.image_(avatar)
            else:
                self.avatar = Image.open(open(avatar, "rb"))
        else:
            raise TypeError(f"avatar must be a path or a file buffer or disnake.Member or nextcord.Member, not {type(background)}") 


        self.avatar = self.avatar.resize((170,170))

        overlay = Image.open("./assets/overlay1.png")
        background = Image.new("RGBA", overlay.size)
        self.backgroundover = self.background.resize((638,159))
        background.paste(self.backgroundover,(0,0))
        
        self.background = background.resize(overlay.size)
        self.background.paste(overlay,(0,0),overlay)

        myFont = ImageFont.truetype("./assets/levelfont.otf",40)
        draw = ImageDraw.Draw(self.background)

        draw.text((205,(327/2)+20), username,font=myFont, fill=text_color,stroke_width=1,stroke_fill=(0, 0, 0))
        bar_exp = (current_exp/max_exp)*420
        if bar_exp <= 50:
            bar_exp = 50    

        current_exp = self.convert_number(current_exp)
        
        max_exp = self.convert_number(max_exp)
        

        myFont = ImageFont.truetype("./assets/levelfont.otf",30)
        draw.text((197,(327/2)+125), f"LEVEL - {self.convert_number(level)}",font=myFont, fill=text_color,stroke_width=1,stroke_fill=(0, 0, 0))

        w,h = draw.textsize(f"{current_exp}/{max_exp}", font=myFont)
        draw.text((638-w-50,(327/2)+125), f"{current_exp}/{max_exp}",font=myFont, fill=text_color,stroke_width=1,stroke_fill=(0, 0, 0))

        mask_im = Image.open("./assets/mask_circle.jpg").convert('L').resize((170,170))
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
        draw.rounded_rectangle((0, 0, bar_exp, 50), 30, fill=bar_color)
        self.background.paste(im, (190, 235))
        new = Image.new("RGBA", self.background.size)
        new.paste(self.background,(0, 0), Image.open("./assets/curvedoverlay.png").convert("L"))
        self.background = new.resize((505, 259))

        if path is not None:
            self.background.save(path, "PNG")
            return path
        else:
            return self.background.tobytes()