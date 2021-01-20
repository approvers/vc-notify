import asyncio
import os
import json
import codecs

import discord

from conf import DISCORD_TOKEN
from functions.create_credential_file import create_credential_file
from functions import firebase
from functions.voice_diff import VoiceDiffHandler


class MainClient(discord.Client):
    """
    Discordクライアント(多重起動防止機構付き)
    """
    def __init__(self, token: str):
        """
        クライアントを起動する前の処理
        tokenとか最初にメッセージ送信するチャンネルの指定をしたりする
        Parameters
        ----------
        token: str
            discordのBotのトークン
        """
        intents = discord.Intents.all()
        intents.members = True
        super(MainClient, self).__init__(presences=True, guild_subscriptions=True, intents=intents)
        self.token = token
        self.voice_diff_handler = VoiceDiffHandler()

    def launch(self):
        """
        clientの起動
        """
        self.run(self.token)

    async def on_message(self, message: discord.Message):
        """
        BOT以外がメッセージを送信したときに関数に処理をさせる
        Parameters
        ----------
        message: discord.Message
            受け取ったメッセージのデータ
        """
        if message.author.bot:
            return

        channel = message.channel
        content = message.content

        if content.lower().startswith("!set kikisen"):
            firebase.set_diff_ch(message.guild.id, channel.id)

    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        target_channel = before.channel if before.channel else after.channel
        try:
            channel_id = firebase.get_diff_ch(target_channel.guild.id)
        except Exception as e:
            print(e)
            return

        diff_channel = self.get_channel(channel_id)

        if not diff_channel:
            return

        await self.voice_diff_handler.handle(diff_channel, member, before, after)


if __name__ == "__main__":
    create_credential_file()
    firebase.init()
    MAIN = MainClient(DISCORD_TOKEN)
    MAIN.launch()
