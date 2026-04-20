import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 561267967946391583

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Бот {bot.user} готов к работе!")

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel

    if channel is not None:
        await channel.send(
            f"👋 Добро пожаловать, {member.mention}!"
        )

        await channel.send(
            "Привет! Если ты уже состоишь в гильдии, то добавь к нику на сервере ник своего персонажа. "
            "Как добавишь — выдам права на приватную часть сервера, где происходит основной движ."
        )

bot.run(TOKEN)