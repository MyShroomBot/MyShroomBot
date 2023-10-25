import discord
import os

from attributes.event_a import event
from classes.BotHandler import BotHandler

join_text = 'Hello there! I am MyShroom, your new companion on this server. I will assist you to accurately identify mushrooms using a powerful IA. **If you ever need assistance, just type "!shroom**".'

class BotClient(discord.Client):
	
	def __init__(self):
		c_prefix = '!'
		c_intents = discord.Intents.default()
		c_intents.message_content = True
		super().__init__(intents = c_intents, command_prefix = c_prefix, help_command=None)
		
		self.handler = BotHandler(self, c_prefix)	
		
	async def on_ready(self):
		print(f'{self.user.name} se ha iniciado correctamente.')

	async def on_message(self, message):
		if os.getenv('Environment','') == 'live' and (message.guild is None 
														or message.guild.id != int(os.getenv('GuildID'))): #CORRECIÓN
			return

		if message.guild.id == '1157074447719735357' and message.channel != '1157112268878774301':
			return

		if message.author == self.user:
			return
		
		await self.handler.messageParser(message)

	@event
	async def on_guild_join(self, guild):
		if guild.system_channel:
			await guild.system_channel.send(join_text)