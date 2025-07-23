import os
import discord
from discord.ext import commands
from flask import Flask
from cmds import register_commands
import threading

# Intents not required unless you add prefix or message commands
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Flask server to keep bot alive on hosts like Render
app = Flask(__name__)
@app.route("/")
def home():
    return "🟢 ZBØT MDTN1 is up!"

def run_flask():
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_flask).start()

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        synced = await bot.tree.sync()
        print(f"🔄 Synced {len(synced)} global slash command(s).")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

# Load all slash commands
register_commands(bot)

# Run
token = os.getenv("DISCORD_TOKEN")
if not token:
    raise RuntimeError("⚠️ DISCORD_TOKEN env var missing")
bot.run(token)