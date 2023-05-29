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