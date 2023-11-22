import json
from asyncio import to_thread as tt

def read_file():
    with open ('src/files/responses.json','r') as file:
        responses  = json.load(file)
    return responses

async def responseHandler(key):
    responses = await tt(read_file)
    return responses[str(key)]