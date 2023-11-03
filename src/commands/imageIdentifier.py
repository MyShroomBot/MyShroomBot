"""
Command for Analyzing Mushroom Images:
Once invoked, you can submit a photo in one of the supported formats (PNG, JPG, JPEG, TIFF, and BMP) with a maximum file size of 10MB.
Subsequently, you will receive a response listing the five most likely mushroom species, organized in descending order of probability.
"""

from asyncio import TimeoutError
from attributes.command_a import command
from attributes.rename_a import rename
from models import decoder
from commands.balance import open_account,getdatabasedata
from modules.progressHandler import checkprogressquest1,checkprogressquest2
from PIL import Image
import requests
from io import BytesIO
import json

valid_types = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp')
image_text = 'Hello! Send me the image you wish me to analize.'
error_noImage = 'Sorry, you did not attach an Image or use a format I do not support.'
error_noValid = 'Sorry, you use a no valid format of Image. Supported types: PNG, JPG, JPEG, TIFF, and BMP'
error_noSize = 'Sorry, your file is above the valid size. Maximum file size: 10MB'
error_noCoins = 'Sorry, you do not have enough coins to use the identification tool. Wait for next week to get more coins or complete quests to earn'

@rename('shroom')
@command
async def imageIdentifier(Client, ctx, extra):
    await ctx.channel.send(image_text)
    def checkerResponse(m):
        return m.attachments and m.channel == ctx.channel and m.author == ctx.author
    try:
        response = await Client.wait_for('message', timeout=60.0, check=checkerResponse)
    except TimeoutError:
        await ctx.channel.send(error_noImage)
        return
    
    attachment = response.attachments[0]
    user = ctx.author
    await open_account(user)
    users = await getdatabasedata()
    if users[str(user.id)]['wallet'] == 0:
        await ctx.channel.send(error_noCoins)
        return
    if not attachment.filename.lower().endswith(valid_types):
        await ctx.channel.send(error_noValid)
        return
    if attachment.size > 10000000:
        await ctx.channel.send(error_noSize)
        return
    Model = decoder.IdentifierModel()
    probs = Model.predict(attachment.url)
    await checkprogressquest1(users,user,ctx)
    probs = str(probs).replace('_',' ')
    if 'Agaricus' in probs:
        await checkprogressquest2(users,user,ctx)
    users[str(user.id)]['wallet'] -= 1
    
    with open('src/files/database.json','w') as f:
        json.dump(users,f)
    if  probs == 'Other':
        answer =  f'Sorry. I did not identify a **mushroom**. Try another image.'
    if probs.startswith('Other'):
        answer = f'You have found a **mushroom!**. This is an {probs}.'
    else:
        answer = f'You have found a **mushroom!**. This is the Scientific name: {probs}.'

    #for prob in probs:
    #   answer += f'> {prob[0]} \n'
    await ctx.channel.send(answer)

imageIdentifier.__doc__ = __doc__