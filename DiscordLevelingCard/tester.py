from io import BytesIO
from typing import Optional, Union

from aiohttp import ClientSession
from PIL import Image, ImageDraw, ImageFont
from .error import InvalidImageUrl
from pathlib import Path
from .card_settings import Settings
from . import RankCard, Sandbox


class Tester:
    """class to test Sandbox and RankCard locally

    Parameters
    ----------
    settings: :class:`Settings`
        The settings for the rank card

    path: :class:`str`
        The path to save the image. Default is `./example`

    cacheing: :class:`bool`
        Whether to cache the image or not. Default is `True`

    avatar: :class:`str`
        The avatar image for the rank card. This can be a path to a file
    
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
    - `path`
    - `max_exp`
    - `rank`

    Methods
    -------
    - `test_card1`
        to test card1 of RankCard
    - `test_card2`
        to test card2 of RankCard
    - `test_card3`
        to test card3 of RankCard
    - `test_sandbox_card1`
        to test custom_card1 of Sandbox


    Raises
    ------
    - `InvalidImageType`
        If the image type is not supported
    - `InvalidImageUrl`
        If the image url is invalid

    """

    __slots__ = ('background', 'path', 'cacheing', 'rank', 'background_color', 'text_color', 'bar_color', 'settings', 'avatar', 'level', 'username', 'current_exp', 'max_exp')

    def __init__(
        self,
        settings: Settings,
        avatar: str,
        level:int,
        username:str,
        current_exp:int,
        max_exp:int,
        path:str = "./example",
        cacheing:bool = True,
        rank:Optional[int] = None

    ):
        self.settings = settings
        self.avatar = avatar
        self.path = path
        self.level = level
        self.rank = rank
        self.username = username
        self.current_exp = current_exp
        self.max_exp = max_exp
        self.cacheing = cacheing
    

    async def test_card1(self, resize: int = 100)->None:
        """test card1 with this method

        Parameters
        ----------
        resize: :class:`int`
            The size to resize the avatar to. Default is `100`

        Attributes
        ----------
        - `resize`
        
        Returns
        -------
        returns nothing but saves a file in the current directory with the given name
        """

        card = RankCard(
            settings=self.settings,
            avatar=Image.open(self.avatar),
            level=self.level,
            username=self.username,
            current_exp=self.current_exp,
            max_exp=self.max_exp,
            rank=self.rank
        )
        card = await card.card1(resize=resize)
        Image.open(card).save(f"{self.path}.png", "PNG")
        return

    async def test_card2(self, resize: int = 100)->None:
        """test card2 with this method

        Parameters
        ----------
        resize: :class:`int`
            The size to resize the avatar to. Default is `100`

        Attributes
        ----------
        - `resize`
        
        Returns
        -------
        returns nothing but saves a file in the current directory with the given name
        """

        card = RankCard(
            settings=self.settings,
            avatar=Image.open(self.avatar),
            level=self.level,
            username=self.username,
            current_exp=self.current_exp,
            max_exp=self.max_exp,
            rank=self.rank
        )
        card = await card.card2(resize=resize)
        Image.open(card).save(f"{self.path}.png", "PNG")
        return

    async def test_card3(self, resize: int = 100)->None:
        """test card3 with this method

        Parameters
        ----------
        resize: :class:`int`
            The size to resize the avatar to. Default is `100`
        
        Attributes
        ----------
        - `resize`
        
        Returns
        -------
        returns nothing but saves a file in the current directory with the given name
        """

        card = RankCard(
            settings=self.settings,
            avatar=Image.open(self.avatar),
            level=self.level,
            username=self.username,
            current_exp=self.current_exp,
            max_exp=self.max_exp,
            rank=self.rank
        )
        card = await card.card3(resize=resize)
        Image.open(card).save(f"{self.path}.png", "PNG")
        return
    
    async def test_sandbox_card1(
            self,
            card_colour: str = "black",
            resize: int = 100
        )->None:
        """test card1 of Sandbox with this method

        Parameters
        ----------
        resize: :class:`int`
            The size to resize the avatar to. Default is `100`

        card_colour: :class:`str`
            The colour of the card. Default is `black`
        
        Attributes
        ----------
        - `card_colour`
        - `resize`
        
        Returns
        -------
        returns nothing but saves a file in the current directory with the given name
        """

        card = Sandbox(
            settings=self.settings,
            avatar=Image.open(self.avatar),
            level=self.level,
            username=self.username,
            current_exp=self.current_exp,
            max_exp=self.max_exp,
            rank=self.rank,
            cacheing=self.cacheing
        )
        card = await card.custom_card1(resize=resize,card_colour=card_colour)
        Image.open(card).save(f"{self.path}.png", "PNG")
        return
    
    async def test_sandbox_card3(
            self,
            resize:int = 100,

            senstivity:int = 200,
            card_colour: str = "black",

            border_width: int = 25,
            border_height: int = 25,
            
            avatar_frame: str = "curvedborder",
            avatar_size: int = 260,
            avatar_position: tuple = (53, 36),
            
            text_font: str = "levelfont.otf",

            username_position: tuple = (330,130),
            username_font_size: int = 50,

            level_position: tuple = (500,40),
            level_font_size: int = 50,

            exp_position: tuple = (775,130),
            exp_font_size: int = 50

        )->None:
        """test card3 of Sandbox with this method

        Parameters
        ----------
        resize: :class:`int`
            The percentage to resize the image to. Default is 100
        
        senstivity: :class:`int`
            Change the transparency of the black box over the background image.
                Default is 200.range - [0,255] 

        border_width: :class:`int`
            width of the border. default is 25

        border_height: :class:`int`
            height of the border. default is 25

        avatar_frame: :class:`str`
            `circle` `square` `curvedborder` `hexagon` or path to a self created mask.
        
        card_colour: :class:`str`
            colour of the translucent overlay. Default is black.

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
        
        Attributes
        ----------
        - `resize`
        - `senstivity`
        - `border_width`
        - `border_height`
        - `avatar_frame`
        - `card_colour`
        - `text_font`
        - `avatar_size`
        - `avatar_position`
        - `username_position`
        - `username_font_size`
        - `level_position`
        - `level_font_size`
        - `exp_position`
        - `exp_font_size`
        
        Returns
        -------
        returns nothing but saves a file in the current directory with the given name
        """

        card = Sandbox(
            settings=self.settings,
            avatar=Image.open(self.avatar),
            level=self.level,
            username=self.username,
            current_exp=self.current_exp,
            max_exp=self.max_exp,
            rank=self.rank,
            cacheing=self.cacheing
        )
        card = await card.custom_card3(
            resize=resize,
            card_colour=card_colour,
            senstivity=senstivity,
            border_width=border_width,
            border_height=border_height,
            avatar_frame=avatar_frame,
            avatar_size=avatar_size,
            avatar_position=avatar_position,
            text_font=text_font,
            username_position=username_position,
            username_font_size=username_font_size,
            level_position=level_position,
            level_font_size=level_font_size,
            exp_position=exp_position,
            exp_font_size=exp_font_size        
        )
        Image.open(card).save(f"{self.path}.png", "PNG")
        return