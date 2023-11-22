"""
Command for providing help:
Gives you assistance with any command or specific command usage. 
Simply type '!help <command>' and you'll receive the information of the commands.
"""

from attributes.command_a import command

help_text = '> help - Provides help. \n > shroom - Analyze Mushroom Images. \n > balance - Checks your MyShroom Coins \n > getquest - Adquire Quests \n > questboard - Check your progress'
error_no_command_text = 'Command not recognized. Type !help for see the commands available.'

@command
async def help(Client, ctx, command_name):
	if not command_name:
			await ctx.channel.send(content=help_text, delete_after=80) 
	else:
		commands = Client.handler.commands
		list_names = list(commands.keys())
		if command_name in list_names:
			doc = commands[command_name].__doc__
			await ctx.channel.send(content=doc, delete_after=80)
		else:
			await ctx.channel.send(content=error_no_command_text, delete_after=80)

help.__doc__ = __doc__