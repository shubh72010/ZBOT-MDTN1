import sys
sys.modules["audioop"] = None  # 🔥 Prevents discord.py from crashing on Python 3.13

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load token from environment (Render has this set in ENV)
TOKEN = os.getenv("DISCORD_TOKEN")

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Bot prefix & setup
bot = commands.Bot(command_prefix="!", intents=intents)

# Ready event
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name} | ID: {bot.user.id}")
    print("Ready to serve in the following guilds:")
    for guild in bot.guilds:
        print(f" • {guild.name} ({guild.id})")

# Basic Ping
@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! Latency: {round(bot.latency * 1000)}ms")

# Uptime
import time
start_time = time.time()

@bot.command()
async def uptime(ctx):
    seconds = int(time.time() - start_time)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    await ctx.send(f"⏱ Uptime: {hours}h {minutes}m {seconds}s")

# User Info
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"{member}'s Info", color=discord.Color.blurple())
    embed.set_thumbnail(url=member.avatar.url if member.avatar else "")
    embed.add_field(name="Display Name", value=member.display_name, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Joined", value=member.joined_at.strftime("%d %b %Y"), inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
    await ctx.send(embed=embed)

# Server Info
@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=f"{guild.name}", color=discord.Color.green())
    embed.set_thumbnail(url=guild.icon.url if guild.icon else "")
    embed.add_field(name="Owner", value=guild.owner, inline=True)
    embed.add_field(name="Members", value=guild.member_count, inline=True)
    embed.add_field(name="ID", value=guild.id, inline=True)
    embed.add_field(name="Created On", value=guild.created_at.strftime("%d %b %Y"), inline=True)
    await ctx.send(embed=embed)

# 8ball
import random

@bot.command()
async def eightball(ctx, *, question):
    responses = [
        "Yes", "No", "Maybe", "Absolutely", "Definitely not",
        "Try again later", "I don't know", "Ask someone else"
    ]
    await ctx.send(f"🎱 {random.choice(responses)}")

# Avatar
@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    if member.avatar:
        await ctx.send(member.avatar.url)
    else:
        await ctx.send("No avatar found.")

# Purge
@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int = 10):
    await ctx.channel.purge(limit=limit + 1)
    await ctx.send(f"🧹 Purged {limit} messages.", delete_after=5)

# Error handler
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to use that.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("⚠️ You're missing an argument.")
    else:
        await ctx.send(f"⚠️ Error: `{str(error)}`")

# Run the bot
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ No DISCORD_TOKEN set in environment variables.")
