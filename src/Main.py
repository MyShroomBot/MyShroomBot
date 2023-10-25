from classes.Client import BotClient
import os

Bot = BotClient()

Bot.run(os.getenv('Token',''))