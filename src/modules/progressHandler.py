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
        