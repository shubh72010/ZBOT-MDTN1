import discord
from discord.ext import commands
from cmds import register_commands
import os
from flask import Flask
import threading

# Bot Setup
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Load Commands
@bot.event
async def on_ready():
    print(f"[+] Logged in as {bot.user}")
    await register_commands(bot)

# Flask Web Server (for Render uptime)
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive!", 200

def run_flask():
    app.run(host="0.0.0.0", port=10000)

# Run Flask in background
threading.Thread(target=run_flask).start()

# Run Discord Bot
bot.run(os.getenv("DISCORD_TOKEN"))