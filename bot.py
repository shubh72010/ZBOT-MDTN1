import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load the .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set up bot with message content intent
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# On bot ready
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name} ({bot.user.id})")

# Basic command: !ping
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# Add more commands below here

# Run the bot
bot.run(TOKEN)