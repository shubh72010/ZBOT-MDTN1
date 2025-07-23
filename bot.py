import os
import discord
from discord.ext import commands, tasks
from discord import app_commands
from flask import Flask
import threading
from cmds import register_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
MY_GUILD = discord.Object(id=123456789012345678)  # Replace with a test server ID for faster updates

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is now online.")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} global commands.")
    except Exception as e:
        print(f"Sync error: {e}")

register_commands(bot)

# Flask server to keep bot alive
app = Flask(__name__)

@app.route("/")
def home():
    return "ZBØT is active!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_flask).start()

bot.run(TOKEN)