"""
Command for Analyzing Mushroom Images:
Once invoked, you can submit a photo in one of the supported formats (PNG, JPG, JPEG, TIFF, and BMP) with a maximum file size of 10MB.
Subsequently, you will receive a response listing the five most likely mushroom species, organized in descending order of probability.
"""

from asyncio import TimeoutError
from attributes.command_a import command
from attributes.rename_a import rename
from models import decoder
from modules.databaseHandler import getUser, modifyCoins
from modules.progressHandler import checkerQ1, checkerQ2
from modules.responseHandler import responseHandler

valid_types = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp')
image_text = 'Hello! Send me the image you wish me to analize. Remember 1 Coin per image!'
error_noImage = 'Sorry, you did not attach an Image or use a format I do not support.'
error_noValid = 'Sorry, you use a no valid format of Image. Supported types: PNG, JPG, JPEG, TIFF, and BMP'
error_noSize = 'Sorry, your file is above the valid size. Maximum file size: 10MB'
error_noCoins = 'Sorry, you do not have enough coins to use the identification tool. Wait for next week to get more coins or complete quests to earn'

@rename('shroom')
@command
async def imageIdentifier(Client, ctx, extra):
    await ctx.channel.send(content=image_text, delete_after=80)
    def checkerResponse(m):
        return m.attachments and m.channel == ctx.channel and m.author == ctx.author
    try:
        response = await Client.wait_for('message', timeout=60.0, check=checkerResponse)
    except TimeoutError:
        await ctx.channel.send(content=error_noImage, delete_after=80)
        return
    
    attachment = response.attachments[0]
    user = ctx.author
    user_data = await getUser(user.id)

    if user_data['wallet'] == 0:
        await ctx.channel.send(content=error_noCoins, delete_after=80)
        return
    if not attachment.filename.lower().endswith(valid_types):
        await ctx.channel.send(content=error_noValid, delete_after=80)
        return
    if attachment.size > 10000000:
        await ctx.channel.send(content=error_noSize, delete_after=80)
        return
    
    Model = decoder.IdentifierModel()
    answer = Model.predict(attachment.url)
    link = await responseHandler(answer)

    await checkerQ1(user.id, ctx)
    answer = str(answer).replace('_',' ')
    if 'Agaricus' in answer:
        await checkerQ2(user.id,ctx)
    
    await modifyCoins(user.id)

    if  answer == 'Other':
        response =  f'Sorry. I did not identify a **mushroom**. Try another image.'
    if answer.startswith('Other'):
        response = f'You have found a **mushroom!**. It is an **{answer}**. You can get more information about it in here: \n {link}'
    else:
        response = f'You have found a **mushroom!**. This is the Scientific name: **{answer}**. You can get more information about it in here: \n {link}'

    await ctx.channel.send(response)

imageIdentifier.__doc__ = __doc__