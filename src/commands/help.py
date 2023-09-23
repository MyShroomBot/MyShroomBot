"""
Command for providing help:
Gives you assistance with any command or specific command usage. 
Simply type '!help <command>' and you'll receive the information of the commands.
"""

from attributes.command_a import command

help_text = '> help - Command for providing help. \n > shroom - Command for Analyzing Mushroom Images.'
error_no_command_text = 'Command not recognized. Type !help for see the commands available.'

@command
async def help(Client, ctx, command_name):
	if not command_name:
		await ctx.channel.send(help_text) #for in docstring.strip().split('\n')[0]
	else:
		commands = Client.handler.commands
		list_names = list(commands.keys())
		if command_name in list_names:
			doc = commands[command_name].__doc__
			await ctx.channel.send(doc)
		else:
			await ctx.channel.send(error_no_command_text)

help.__doc__ = __doc__