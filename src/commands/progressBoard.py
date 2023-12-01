"""
Command for Checking your Progress on Quests:
Check how far have you go in your Quests. Remember to active your quests using !getquest.
"""

from attributes.command_a import command
from attributes.rename_a import rename
from attributes.command_a import command
from attributes.rename_a import rename
from modules.databaseHandler import getUser
from discord import Embed, Colour

@rename('questboard')
@command
async def questboard(Client, ctx, extra):
    user = ctx.author
    user_data = await getUser(user.id)
    Q1Adv = user_data['quest1']
    Q2Adv = user_data['quest2']

    em = Embed(title = f"{ctx.author.name}s quests", color = Colour.teal())
    if Q1Adv >= 0:
        em.add_field(name = "Quest 1", value = str(Q1Adv) + '/3 completed')
    else:
        em.add_field(name = "Quest 1", value = 'Not started')
    if Q2Adv >= 0:
        em.add_field(name = "Quest 2", value = str(Q2Adv) + '/3 completed')
    else:
        em.add_field(name = "Quest 2", value = 'Not started')
    em.set_thumbnail(url = user.avatar)
    await ctx.reply(embed = em)

questboard.__doc__ = __doc__