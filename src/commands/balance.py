"""
Command for Checking your MyShroom Coins:
Once invoked, you can check your balances of coins for analyzing Mushrooms images. Remember if you do not have Coins you can't analyze!
"""

from discord.ext import commands
from attributes.command_a import command
from attributes.rename_a import rename
from discord import Embed, Colour, Member
from modules.databaseHandler import getUser, modifyCoins

coinamountmessage = 'How many coins do you wish to give '
error_noReply = 'Sorry, we did not receive a response in the time window'

@rename('balance')
@command
async def balance(Client, ctx, extra):
    user = ctx.author
    user_data = await getUser(user.id)
    wallet_amount = user_data["wallet"]
    em = Embed(title = f"{ctx.author.name}'s balance", color = Colour.red())
    em.add_field(name = "Wallet Balance", value = str(wallet_amount) + ' ShroomCoins')
    em.set_thumbnail(url = user.avatar)
    await ctx.channel.send(embed = em)

@rename('give')
@command
@commands.has_permissions(kick_members=True)
async def give(Client, ctx, member: Member):
    identification = member.replace("<","").replace(">","").replace("@","")
    user = await Client.fetch_user(identification)
    await ctx.reply(coinamountmessage + str(user.name) + '?', delete_after=90)
    def checkerResponse(m):
        return m.content and m.channel == ctx.channel and m.author == ctx.author
    try:
        coin_amount = await Client.wait_for('message', timeout=60.0, check=checkerResponse)
        coin_amount = int(coin_amount.content)
    except TimeoutError:
        await ctx.reply(error_noReply, delete_after=90)
        return
    await modifyCoins(identification, coin_amount)
    await ctx.channel.send(f"Someone gave you {coin_amount} Shroomcoins!!")

balance.__doc__ = __doc__