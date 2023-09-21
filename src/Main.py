from classes.Client import Client
import os

Bot = Client()

Bot.run(os.getenv('Token'))