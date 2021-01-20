"""
はらちょの根幹ファイル
"""
import asyncio
import os
import json
import codecs

import discord


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
        if message.author.bot and not message.author.id in MainClient.CLI_BOTS:
            return
        channel = message.channel
        message_str = message.content
        pass

    async def on_voice_state_update(self, member, before, after):
        pass


if __name__ == "__main__":
    TOKEN = os.environ["TOKEN"]
    MAIN = MainClient(TOKEN)
    MAIN.launch()
