from classes.Client import BotClient
import os
from dotenv import load_dotenv

Bot = BotClient()
load_dotenv()

Bot.run(os.getenv('Token',''))