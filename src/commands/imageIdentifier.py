from attributes.command_a import command
from attributes.rename_a import rename

from PIL import Image
import os

valid_types = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp')
image_text = 'Hello! Send me the image you wish me to analize.'
error_noImage = 'Sorry, you did not attach an Image or use a format I do not support.'
error_noValid = 'Sorry, you use a no valid format of Image. Supported types: png, jpg, jpeg, tiff and bmp'
error_noSize = 'Sorry, your file is above the valid size. Maximum file size: 10MB'

@rename('shroom')
@command
async def imageIdentifier(Client, ctx, command_name):
    await ctx.send(image_text)
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
    
    attachment.url #Conexión base de datos