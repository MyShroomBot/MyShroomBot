from modules.databaseHandler import getUser, modifyCoins, modifyQuests

quest_complete = 'Congratulations! you completed the quest! Check your balance to see your rewards!'

async def checkerQ1(id, ctx):
    user_data = await getUser(str(id))
    if (user_data['quest1'] < 3) and (user_data['quest1'] > -1) :
        await modifyQuests(str(id),'quest1')
        if user_data['quest1'] == 2:
            await modifyCoins(str(id),amount=5)
            await ctx.reply(content=quest_complete)

async def checkerQ2(id,ctx):
    user_data = await getUser(str(id))
    if (user_data['quest2'] < 2) and (user_data['quest2'] > -1) :
        await modifyQuests(str(id),'quest1')
        if user_data['quest1'] == 1:
            await modifyCoins(str(id),amount=5)
            await ctx.reply(content=quest_complete)
        