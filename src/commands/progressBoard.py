"""
Command for Checking your Progress on Quests:
Check how far have you go in your Quests. Remember to active your quests using !getquest.
"""

import json
from discord.ext import commands
from attributes.command_a import command
from attributes.rename_a import rename
from asyncio import TimeoutError
from attributes.command_a import command
from attributes.rename_a import rename
from models import decoder
from commands.balance import open_account,getdatabasedata
import json
import discord

@rename('questboard')
@command
async def questboard(Client,ctx, extra):
    user = ctx.author
    await open_account(user)
    users = await getdatabasedata()
    quest1prog = users[str(user.id)]['quest1']
    quest2prog = users[str(user.id)]['quest2']
    em = discord.Embed(title = f"{ctx.author.name}s quests", color = discord.Colour.teal())
    em.add_field(name = "Quest 1", value = str(quest1prog) + '/3 completed' )
    em.add_field(name = "Quest 2", value = str(quest2prog) + '/3 completed')
    em.set_thumbnail(url = user.avatar)
    await ctx.channel.send(embed = em)

questboard.__doc__ = __doc__