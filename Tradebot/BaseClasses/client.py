
import discord
from .secrets_loader import SecretsLoader

class MyClient(discord.Client):
    def __init__(self):
        self.token = self.load_token()

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    def load_token(self):
        secrets = SecretsLoader()
        secrets.load_secrets('secrets.json')