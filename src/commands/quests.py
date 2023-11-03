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

error_noReply = 'Sorry, we did not receive a response in the time window'
quest_text = 'Welcome to the Myshroom quest board, where you can earn ShroomCoins by going on adventures!\nType the number of one of the following quests to begin you new adventure:\n1. Succesfully identify 2 different mushroom species (reward: 5 ShroomCoins)\n2. Succesfully identify 3 mushroom varieties from the Agaricus family (reward: 5 ShroomCoins)'
quest_in_progress = 'Sorry, you already finished or accepted his quest'
quest_complete = 'Congratulations! you completed the quest! Check your balance to see your rewards!'
@rename('getquest')
@command
async def getquest(Client,ctx, extra):
    user = ctx.author
    await open_account(user)
    users = await getdatabasedata()
    await ctx.channel.send(quest_text)
    def checkerResponse(m):
        return m.content and m.channel == ctx.channel and m.author == ctx.author
    try:
        response = await Client.wait_for('message', timeout=60.0, check=checkerResponse)
    except TimeoutError:
        await ctx.channel.send(error_noReply)
        return
    response = int(response.content)
    if (response == 1 ):
        if (users[str(user.id)]['quest1']==0):
            users[str(user.id)]['quest1'] += 1
            await ctx.channel.send('You accepted quest 1, good luck on you new adventure!')
        else:
            await ctx.channel.send(quest_in_progress)
        
    if (response == 2 ):
        if(users[str(user.id)]['quest2']==0):
            users[str(user.id)]['quest2'] += 1
            await ctx.channel.send('You accepted quest 2, good luck on you new adventure!')
        else:
            await ctx.channel.send(quest_in_progress)
    with open('src/files/database.json','w') as f:
        json.dump(users,f)
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

async def checkprogressquest1(users,user,ctx):
    if (users[str(user.id)]['quest1'] < 3) and (users[str(user.id)]['quest1'] > 0) :
        users[str(user.id)]['quest1'] += 1
        if users[str(user.id)]['quest1'] == 3:
            users[str(user.id)]['wallet'] +=5
            await ctx.channel.send(quest_complete)
    with open('src/files/database.json','w') as f:
        json.dump(users,f)
async def checkprogressquest2(users,user,ctx):
    if (users[str(user.id)]['quest2'] < 3) and (users[str(user.id)]['quest2'] > 0) :
        users[str(user.id)]['quest2'] += 1
        if users[str(user.id)]['quest2'] == 3:
            users[str(user.id)]['wallet'] +=5
            await ctx.channel.send(quest_complete)
    with open('src/files/database.json','w') as f:
        json.dump(users,f)
        
    
