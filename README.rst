DiscordLevelingCard
===================

A library with Rank cards for your discord bot.

.. raw:: html

   <h3 style="color:yellow;">

now create your own custom rank cards!

.. raw:: html

   </h3>

|Downloads|

card preview
============

``card1``

.. figure:: https://user-images.githubusercontent.com/77439837/234198272-3dcaabb0-0f38-4d51-9938-de4b0ad42123.png
   :alt: card1

   card1

``card2`` |card2|

``card3`` *same as card2 but with background* |card3|

installation
============

``for pypi version``

.. code:: sh

   pip install discordlevelingcard

``for github developement version``

.. code:: sh

   pip install git+https://github.com/krishsharma0413/DiscordLevelingCard

How To Use
==========

If you don’t provide ``path`` then the method will return ``bytes``
which can directly be used in discord.py/disnake/pycord/nextcord ’s
``File class``.

Example
=======

``since no path was provided, it returns bytes which can directly be used in discord.py and its fork's File class.``

.. code:: py

   from disnake.ext import commands
   from DiscordLevelingCard import RankCard, Settings
   import disnake

   client = commands.Bot()
   # define background, bar_color, text_color at one place
   card_settings = Settings(
       background="url or path to background image",
       text_color="white",
       bar_color="#000000"
   )

   @client.slash_command(name="rank")
   async def user_rank_card(ctx, user:disnake.Member):
       await ctx.response.defer()
       a = RankCard(
           settings=card_settings,
           avatar=user.display_avatar.url,
           level=1,
           current_exp=1,
           max_exp=1,
           username="cool username"
       )
       image = await a.card1()
       await ctx.edit_original_message(file=disnake.File(image, filename="rank.png")) # providing filename is very important

Documentation
-------------

.. raw:: html

   <details>

.. raw:: html

   <summary>

RankCard class

.. raw:: html

   </summary>

``__init__`` method

.. code:: py

   RankCard(
       settings: Settings,
       avatar:str,
       level:int,
       current_exp:int,
       max_exp:int,
       username:str,
       rank: Optional[int] = None
   )

-  ``settings`` - Settings class from DiscordLevelingCard.

-  ``avatar`` - avatar image url.

-  ``level`` - level of the user.

-  ``current_exp`` - current exp of the user.

-  ``max_exp`` - max exp of the user.

-  ``username`` - username of the user.

-  ``rank`` - rank of the user. (optional)

methods
-------

-  ``card1``
-  ``card2``
-  ``card3``

.. raw:: html

   </details>

.. raw:: html

   <details>

.. raw:: html

   <summary>

Sandbox class

.. raw:: html

   </summary>

``__init__`` method

.. code:: py

   RankCard(
       settings: Settings,
       avatar:str,
       level:int,
       current_exp:int,
       max_exp:int,
       username:str,
       cacheing:bool = True,
       rank: Optional[int] = None
   )

-  ``settings`` - Settings class from DiscordLevelingCard.

-  ``avatar`` - avatar image url.

-  ``level`` - level of the user.

-  ``current_exp`` - current exp of the user.

-  ``max_exp`` - max exp of the user.

-  ``username`` - username of the user.

-  ``rank`` - rank of the user. (optional)

-  ``cacheing`` - if set to ``True`` then it will cache the image and
   will not regenerate it again. (default is ``True``)

.. _methods-1:

methods
-------

-  ``custom_card1``

.. raw:: html

   </details>

.. raw:: html

   <details>

.. raw:: html

   <summary>

Settings class

.. raw:: html

   </summary>

``__init__`` method

.. code:: py

   Settings(
       background: Union[PathLike, BufferedIOBase, str],
       bar_color: Optional[str] = 'white',
       text_color: Optional[str] = 'white',
       background_color: Optional[str]= "#36393f"

   )

-  ``background`` - background image url or file-object in ``rb`` mode.

   -  ``4:1`` aspect ratio recommended.

-  ``bar_color`` - color of the bar [example: “white” or “#000000”]

-  ``text_color`` - color of the text [example: “white” or “#000000”]

-  ``background_color`` - color of the background [example: “white” or
   “#000000”]

.. raw:: html

   </details>

.. raw:: html

   <details>

.. raw:: html

   <summary>

card1 method

.. raw:: html

   </summary>

.. code:: py

   RankCard.card1(resize: int = 100)

attribute
---------

-  ``resize`` : resize the final image. (default is 100, treat it as a
   percentage.)

returns
-------

-  ``bytes`` which can directly be used within ``discord.File`` class.

.. figure:: https://user-images.githubusercontent.com/77439837/234198272-3dcaabb0-0f38-4d51-9938-de4b0ad42123.png
   :alt: card1

   card1

.. raw:: html

   </details>

.. raw:: html

   <details>

.. raw:: html

   <summary>

card2 method

.. raw:: html

   </summary>

.. code:: py

   RankCard.card2(resize: int = 100)

.. _attribute-1:

attribute
---------

-  ``resize`` : resize the final image. (default is 100, treat it as a
   percentage.)

.. _returns-1:

returns
-------

-  ``bytes`` which can directly be used within ``discord.File`` class.

.. figure:: https://user-images.githubusercontent.com/77439837/234198354-315e9420-9bd7-47bd-87ed-b21c3772646c.png
   :alt: card

   card

.. raw:: html

   </details>

.. raw:: html

   <details>

.. raw:: html

   <summary>

card3 method

.. raw:: html

   </summary>

.. code:: py

   RankCard.card3(resize: int = 100)

.. _attribute-2:

attribute
---------

-  ``resize`` : resize the final image. (default is 100, treat it as a
   percentage.)

.. _returns-2:

returns
-------

-  ``bytes`` which can directly be used within ``discord.File`` class.

.. figure:: https://user-images.githubusercontent.com/77439837/234203410-a6a970ef-c01c-454b-be67-6dc7c1b2c807.png
   :alt: card3

   card3

.. raw:: html

   </details>

.. raw:: html

   <details>

.. raw:: html

   <summary>

custom_card1 method

.. raw:: html

   </summary>

.. code:: py

   Sandbox.custom_card1(card_colour:str = "black", resize: int = 100)

.. _attribute-3:

attribute
---------

-  ``resize`` : resize the final image. (default is 100, treat it as a
   percentage.)
-  ``card_colour`` : color of the card. (default is black)

.. _returns-3:

returns
-------

-  ``bytes`` which can directly be used within ``discord.File`` class.

examples
--------

.. figure:: https://raw.githubusercontent.com/krishsharma0413/DiscordLevelingCard/main/Examples/custom%20card%20examples/blue_card1.png
   :alt: custom_card1

   custom_card1

.. figure:: https://raw.githubusercontent.com/krishsharma0413/DiscordLevelingCard/main/Examples/custom%20card%20examples/white_card1.png
   :alt: custom_card1

   custom_card1

.. figure:: https://raw.githubusercontent.com/krishsharma0413/DiscordLevelingCard/main/Examples/custom%20card%20examples/black_card1.png
   :alt: custom_card1

   custom_card1

.. raw:: html

   </details>

.. raw:: html

   <details>

.. raw:: html

   <summary>

custom_card3 method

.. raw:: html

   </summary>

.. code:: py

   Sandbox.custom_card3(
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
       exp_font_size: int = 50,

   )

.. _attribute-4:

attribute
---------

-  ``resize`` : resize the final image. (default is 100, treat it as a
   percentage.)
-  ``senstivity`` : senstivity of the avatar frame. (default is 200)
-  ``card_colour`` : color of the card. (default is black)
-  ``border_width`` : width of the border. (default is 25)
-  ``border_height`` : height of the border. (default is 25)
-  ``avatar_frame`` : avatar frame. (default is “curvedborder”)
-  ``avatar_size`` : size of the avatar. (default is 260)
-  ``avatar_position`` : position of the avatar. (default is (53, 36))
-  ``text_font`` : font of the text. (default is “levelfont.otf”)
-  ``username_position`` : position of the username. (default is
   (330,130))
-  ``username_font_size`` : font size of the username. (default is 50)
-  ``level_position`` : position of the level. (default is (500,40))
-  ``level_font_size`` : font size of the level. (default is 50)
-  ``exp_position`` : position of the exp. (default is (775,130))
-  ``exp_font_size`` : font size of the exp. (default is 50)

.. _returns-4:

returns
-------

-  ``bytes`` which can directly be used within ``discord.File`` class.

.. _examples-1:

examples
--------

.. figure:: https://raw.githubusercontent.com/krishsharma0413/DiscordLevelingCard/main/Examples/custom%20card%20examples/custom%20card3%20example-1.png
   :alt: custom_card3

   custom_card3

.. figure:: https://raw.githubusercontent.com/krishsharma0413/DiscordLevelingCard/main/Examples/custom%20card%20examples/custom%20card3%20unholy%20example-2.png
   :alt: custom_card3

   custom_card3

.. raw:: html

   </details>

if you want to see changelog then click
`here <https://github.com/krishsharma0413/DiscordLevelingCard/blob/main/CHANGELOG.md>`__

please star the repository if you like it :D

.. |Downloads| image:: https://pepy.tech/badge/discordlevelingcard
   :target: https://pepy.tech/project/discordlevelingcard
.. |card2| image:: https://user-images.githubusercontent.com/77439837/234198354-315e9420-9bd7-47bd-87ed-b21c3772646c.png
.. |card3| image:: https://user-images.githubusercontent.com/77439837/234203410-a6a970ef-c01c-454b-be67-6dc7c1b2c807.png
