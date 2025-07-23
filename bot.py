import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from cmds import setup_commands
from flask import Flask
import threading

# Load token from environment
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Load slash & normal commands
@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")
    await setup_commands(bot)

# Web server (keeps bot alive on Render)
app = Flask("")

@app.route("/")
def home():
    return "ZBØT-MDTN1 running."

def run():
    app.run(host="0.0.0.0", port=8080)

# Keep-alive thread
threading.Thread(target=run).start()

# Start bot
if TOKEN:
    bot.run(TOKEN)
else:
    print("Missing DISCORD_BOT_TOKEN in environment variables.")