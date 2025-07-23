import os
import discord
from discord.ext import commands
from cmds import setup_commands  # ✅ Fixed: importing the correct function

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)  # prefix is ignored

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        synced = await bot.tree.sync()
        print(f"🌍 Synced {len(synced)} global slash commands.")
    except Exception as e:
        print(f"⚠️ Failed to sync slash commands: {e}")
    
    await setup_commands(bot)

# Get token from environment (set this on Render)
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is missing from environment.")
bot.run(TOKEN)