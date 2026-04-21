import discord
from discord.ext import commands
import os
from flask import Flask
import threading

# --- Flask сервер ---
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# запускаем Flask в отдельном потоке
threading.Thread(target=run_web).start()

# --- Discord бот ---
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1468628687384612950

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

    if channel:
        await channel.send(
            f"👋 Добро пожаловать, {member.mention}!"
        )

        await channel.send(
            "Привет! Если ты уже состоишь в гильдии, то добавь к нику на сервере ник своего персонажа."
        )

bot.run(TOKEN)