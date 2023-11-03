"""
Command for Checking your MyShroom Coins:
Once invoked, you can check your balances of coins for analyzing Mushrooms images. Remember if you do not have Coins you can't analyze!
"""
import json
from discord.ext import commands
from attributes.command_a import command
from attributes.rename_a import rename
import discord
coinamountmessage = 'How many coins do you wish to give '
error_noReply = 'Sorry, we did not receive a response in the time window'
@rename('balance')
@command
async def balance(Client,ctx, extra):
    user = ctx.author
    await open_account(user)
    users = await getdatabasedata()
    wallet_amount=users[str(user.id)]["wallet"]
    em = discord.Embed(title = f"{ctx.author.name}'s balance", color = discord.Colour.red())
    em.add_field(name = "Wallet Balance", value = str(wallet_amount) + ' ShroomCoins')
    em.set_thumbnail(url = user.avatar)
    await ctx.channel.send(embed = em)

@rename('give')
@command
@commands.has_permissions(kick_members=True)
async def give(Client, ctx, member: discord.Member):
    identification = member.replace("<","").replace(">","").replace("@","")
    user = await Client.fetch_user(identification)
    await ctx.channel.send(coinamountmessage + str(user.name) + '?')
    def checkerResponse(m):
        return m.content and m.channel == ctx.channel and m.author == ctx.author
    try:
        coin_amount = await Client.wait_for('message', timeout=60.0, check=checkerResponse)
        coin_amount = int(coin_amount.content)
    except TimeoutError:
        await ctx.channel.send(error_noReply)
        return
    await open_account(user)
    users = await getdatabasedata()
    users[str(identification)]['wallet'] += coin_amount
    await ctx.channel.send(f"Someone gave you {coin_amount} Shroomcoins!!")
    with open('src/files/database.json','w') as f:
        json.dump(users,f)

async def open_account(user):
    users = await getdatabasedata()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['wallet'] = 5
        users[str(user.id)]['quest1'] = 0
        users[str(user.id)]['quest2'] = 0
    with open('src/files/database.json','w') as f:
        json.dump(users,f)
    return True

async def getdatabasedata():
    with open ('src/files/database.json','r') as f:
        users  = json.load(f)
    return users

balance.__doc__ = __doc__