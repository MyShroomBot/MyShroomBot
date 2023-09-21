import discord
import os

from classes.BotHandler import BotHandler

class Client(discord.Client):
	
	def __init__(self):
		c_prefix = '!'
		c_intents = discord.Intents.default()
		c_intents.messages = True
		super().__init__(intents = c_intents, command_prefix = c_prefix, help_command=None)
		
		self.handler = BotHandler(Client, c_prefix)	
		
	async def on_ready(self):
		print(f'{self.user.name} se ha iniciado correctamente.')

	async def on_message(self, message):
		if os.getenv('Environment') == 'testing' and (message.guild is None or message.guild.id != os.getenv('GuildID')):
			return

		if message.author == self.user:
			return

		await self.handler.messageParser(message)