import discord

from config import DISCORD_TOKEN
from src.util.singleton import Singleton


class Client(discord.Client, Singleton):
    def __init__(self):
        intents = discord.Intents.all()
        intents.members = True
        super(Client, self).__init__(presences=True, guild_subscriptions=True, intents=intents)

    def launch(self):
        self.run(DISCORD_TOKEN)

    async def on_ready(self):
        pass

    async def on_message(self):
        pass

    async def on_voice_state_update(self):
        pass
