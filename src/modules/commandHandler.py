def commandHandler(msgInfo, prefix, commands):
	message = msgInfo.content
	words = message.split
	command_name = words[0][len(prefix):]
	response = None
	if len(words) > 1:
		response = words[1:]
	return commands[command_name], response