import discord
from discord.ext import commands
import asyncio
import os

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 561267967946391583

# 1. Включаем ВСЕ необходимые намерения
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # <-- ВАЖНО: Без этого on_member_join не сработает!

bot = commands.Bot(command_prefix="!", intents=intents)

# --- Обработчик готовности бота (уже был) ---
@bot.event
async def on_ready():
    print(f"Бот {bot.user} готов к работе!")
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Бот запущен и готов к отправке уведомлений!")

# --- НОВЫЙ ОБРАБОТЧИК: Приветствие нового участника ---
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel

    if channel is not None:
        # Первое сообщение
        await channel.send(
            f"👋 Добро пожаловать, {member.mention}! Рады видеть тебя на сервере."
        )

        # Второе сообщение
        await channel.send(
            "Привет! Если ты уже состоишь в гильдии, то добавь к нику на сервере ник своего персонажа. "
            "Как добавишь — выдам права на приватную часть сервера, где происходит основной движ."
        )
bot.run(TOKEN)