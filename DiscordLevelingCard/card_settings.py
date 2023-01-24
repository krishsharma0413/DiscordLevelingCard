from io import BufferedIOBase, IOBase, BytesIO
from os import PathLike
from typing import Optional, Union
from .error import InvalidImageType, InvalidImageUrl
from requests import get
from PIL import Image


class Settings:
    """
    Represents the settings for the rank card

    Parameters
    ----------
    background: :class:`Optional[Union[PathLike, BufferedIOBase, str]]`
        The background image for the rank card. This can be a path to a file or a file-like object in `rb` mode or URL or HEX depending upon the card

    bar_color: :class:`Optional[str]`
        The color of the XP bar. This can be a hex code or a color name. Default is `white`
    
    text_color: :class:`Optional[str]`
        The color of the text. This can be a hex code or a color name. Default is `white`
    
    background_color: :class:`Optional[str]`
        The color of the background. This can be a hex code or a color name. Default is `#36393f`

    Attributes
    ----------
    - `background`
    - `bar_color`
    - `text_color`
    - `background_color`
    """

    __slots__ = ('background', 'bar_color', 'text_color', 'background_color')

    def __init__(
        self,
        background: Optional[Union[PathLike, BufferedIOBase, str]]=None,
        background_color: Optional[str]= "#36393f",
        bar_color: Optional[str] = 'white',
        text_color: Optional[str] = 'white'
    ) -> None:
        self.background = background
        self.bar_color = bar_color
        self.text_color = text_color
        self.background_color = background_color

        if isinstance(self.background, IOBase):
            if not (self.background.seekable() and self.background.readable() and self.background.mode == "rb"):
                raise InvalidImageType(f"File buffer {self.background!r} must be seekable and readable and in binary mode")
            self.background = Image.open(self.background)
        elif isinstance(self.background, str):
            if self.background.startswith("http"):
                self.background = Settings._image(self.background)
            else:
                self.background = Image.open(open(self.background, "rb"))
        else:
            raise InvalidImageType(f"background must be a path or url or a file buffer, not {type(self.background)}") 

    @staticmethod
    def _image(url:str):
        response = get(url)
        if response.status_code != 200:
            raise InvalidImageUrl(f"Invalid image url: {url}")
        return Image.open(BytesIO(response.content))
