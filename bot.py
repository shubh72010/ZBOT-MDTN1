import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from cmds import SlashCmds  # Import your commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree  # Slash command tree

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        await tree.sync()
        print("✅ Slash commands synced globally")
    except Exception as e:
        print(f"❌ Slash command sync failed: {e}")

# Register all commands
SlashCmds(tree)

bot.run(TOKEN)