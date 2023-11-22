"""
Command for Adquiring Quests:
Here you can get differents quests so you can earn the MyShroom Coins! 
After using it just type the number of the quest you like the most and go for it! 
"""

from attributes.command_a import command
from attributes.rename_a import rename
from asyncio import TimeoutError
from attributes.command_a import command
from attributes.rename_a import rename
from modules.databaseHandler import getUser, modifyQuests

error_noReply = 'Sorry, we did not receive a response in the time window'
quest_text = 'Welcome to the Myshroom quest board, where you can earn ShroomCoins by going on adventures!\nType the number of one of the following quests to begin you new adventure:\n1. Succesfully identify 3 mushrooms (reward: 5 ShroomCoins)\n2. Succesfully identify 2 mushroom varieties from the Agaricus family (reward: 5 ShroomCoins)'
quest_in_progress = 'Sorry, you already finished or accepted his quest'

@rename('getquest')
@command
async def getquest(Client, ctx, extra):
    user = ctx.author
    user_data = await getUser(user.id)
    await ctx.channel.send(content=quest_text, delete_after=80)

    def checkerResponse(m):
        return m.content and m.channel == ctx.channel and m.author == ctx.author
    try:
        response = await Client.wait_for('message', timeout=60.0, check=checkerResponse)
    except TimeoutError:
        await ctx.channel.send(content=error_noReply, delete_after=80)
        return
    
    response = int(response.content)
    if (response == 1):
        if (user_data['quest1'] == -1):
            await modifyQuests(user.id, 'quest1')
            await ctx.channel.send('You accepted quest 1, good luck on you new adventure!')
        else:
            await ctx.channel.send(content=quest_in_progress, delete_after=80)
        
    if (response == 2):
        if(user_data['quest2']==-1):
            await modifyQuests(user.id, 'quest2')
            await ctx.channel.send('You accepted quest 2, good luck on you new adventure!')
        else:
            await ctx.channel.send(content=quest_in_progress, delete_after=80)

getquest.__doc__ = __doc__