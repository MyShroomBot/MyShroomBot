import json
from asyncio import to_thread as tt

def read_file():
    with open('src/files/database.json', 'r') as file:
        return json.load(file)

def save_file(users):
    with open('src/files/database.json', 'w') as file:
        json.dump(users, file)

async def getUser(id):
    users = await tt(read_file)
    try:
        user = users[str(id)]
    except Exception: #Welcome User - May change
        users[str(id)] = {}
        users[str(id)]['wallet'] = 5
        users[str(id)]['quest1'] = -1
        users[str(id)]['quest2'] = -1
        await tt(save_file,users)
        user = users[str(id)]
    return user

async def modifyCoins(id, amount=-1):
    await getUser(id)
    users = await tt(read_file)
    users[str(id)]['wallet'] += amount
    await tt(save_file, users)

async def modifyQuests(id, quest, quantity=1):
    users = await tt(read_file)
    users[str(id)][quest] += quantity
    await tt(save_file, users)
        
    
    