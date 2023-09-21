def messageHandler(msgInfo, prefix: str):
    message = msgInfo.content
    if not message:
        return None
    if message.startswith(prefix):
        return True
    return False