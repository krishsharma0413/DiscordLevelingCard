from io import BufferedIOBase
from os import PathLike
from typing import Optional, Union

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