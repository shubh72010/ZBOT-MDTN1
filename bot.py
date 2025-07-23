import os
import discord
from discord.ext import commands
from cmds import setup_commands

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)  # Prefix ignored, slash only

@client.event
async def on_ready():
    print(f"Logged in as {client.user} ({client.user.id})")
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} slash commands globally.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

    await setup_commands(client)

# Read bot token from Render environment
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN not set in environment.")
client.run(TOKEN)