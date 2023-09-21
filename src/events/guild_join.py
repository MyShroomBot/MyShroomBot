from attributes.event_a import event

join_text = 'Hello there! I am MyShroom, your new companion on this server. I will assist you to accurately identify mushrooms using a powerful IA. If you ever need assistance, just type "!Shroom".'

@event
async def on_guild_join(guild):
    if guild.system_channel:
        await guild.system_channel.send(join_text)