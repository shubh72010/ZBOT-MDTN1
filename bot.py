import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def echo(ctx, *, msg):
    await ctx.send(msg)

bot.run(TOKEN)