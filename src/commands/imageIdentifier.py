"""
Command for Analyzing Mushroom Images:
Once invoked, you can submit a photo in one of the supported formats (PNG, JPG, JPEG, TIFF, and BMP) with a maximum file size of 10MB.
Subsequently, you will receive a response listing the five most likely mushroom species, organized in descending order of probability.
"""

from attributes.command_a import command
from attributes.rename_a import rename

valid_types = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp')
image_text = 'Hello! Send me the image you wish me to analize.'
error_noImage = 'Sorry, you did not attach an Image or use a format I do not support.'
error_noValid = 'Sorry, you use a no valid format of Image. Supported types: PNG, JPG, JPEG, TIFF, and BMP'
error_noSize = 'Sorry, your file is above the valid size. Maximum file size: 10MB'

@rename('shroom')
@command
async def imageIdentifier(Client, ctx, extra):
    await ctx.channel.send(image_text)
    def checkerResponse(m):
        return m.attachments and m.channel == ctx.channel and m.author == ctx.author
    response = await Client.wait_for('message', timeout=30.0, check=checkerResponse)

    if not response:
        await ctx.channel.send(error_noImage)
        return
    
    attachment = response.attachments[0]

    if not attachment.filename.lower().endswith(valid_types):
        await ctx.channel.send(error_noValid)
        return
    if attachment.size > 10000000:
        await ctx.channel.send(error_noSize)
        return
    
    probs = model.analize(attachment.url) #Conexión base de datos

    answer = ''
    for prob in probs:
        answer += f'> {prob[0]} \n'
    await ctx.channel.send(answer)

imageIdentifier.__doc__ = __doc__