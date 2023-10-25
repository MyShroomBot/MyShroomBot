from commands.help import help 
from commands.imageIdentifier import imageIdentifier

from events.guild_join import on_guild_join

from modules.messageHandler import messageHandler
from modules.commandHandler import commandHandler
from modules.eventHandler import eventHandler

class BotHandler:

  def __init__(self, Client, prefix):
    commands = [help, imageIdentifier]
    commands_name = [c.__name__ for c in commands]

    self.commands = dict(zip(commands_name, commands))
    #self.events = [on_guild_join]
    #self.modules = [commandHandler, eventHandler, messageHandler]
    self.client = Client
    self.prefix = prefix

  async def messageParser(self, msgInfo):
    interaction_type = messageHandler(msgInfo, self.prefix)

    if interaction_type is None:
        # If no interaction type was found, return
        return

    if interaction_type:
        command, response = commandHandler(msgInfo, self.prefix, self.commands)
        await command(self.client, msgInfo, response)
    else:
        # If no command was found, handle the event
        await eventHandler(msgInfo)
    
