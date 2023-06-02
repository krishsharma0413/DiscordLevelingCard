from typing import Optional, Union, List

from PIL import Image
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
    
    async def test_sandbox_custom_canvas(
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

        )->None:
        """test card3 of Sandbox with this method

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
        card = await card.custom_canvas(
            has_background=has_background,
            background_colour=background_colour,
            canvas_size=canvas_size,
            resize=resize,
            overlay=overlay,
            avatar_frame=avatar_frame,
            avatar_size=avatar_size,
            avatar_position=avatar_position,
            text_font=text_font,
            username_position=username_position,
            username_font_size=username_font_size,
            level_position=level_position,
            level_font_size=level_font_size,
            exp_position=exp_position,
            exp_font_size=exp_font_size,
            exp_bar_width=exp_bar_width,
            exp_bar_height=exp_bar_height,
            exp_bar_background_colour=exp_bar_background_colour,
            exp_bar_position=exp_bar_position,
            exp_bar_curve=exp_bar_curve,
            extra_text=extra_text,
            exp_bar=bar_exp
            
        )
        Image.open(card).save(f"{self.path}.png", "PNG")
        return