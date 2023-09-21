from attributes.command_a import command

help_text = '> Ayuda'
error_no_command_text = 'Command not recognized. Type !help for see the commands available.'

@command
async def help(Client, ctx, command_name):
	if not command_name:
		await ctx.channel.send(help_text)
	else:
		commands = Client.handler.commands
		list_names = list(commands.keys())
		if command_name in list_names:
			doc = commands[command_name].__doc__ #Info del Comando
			await ctx.channel.send(doc)
		else:
			await ctx.channel.send(error_no_command_text)