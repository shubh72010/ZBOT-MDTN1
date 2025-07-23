import os
import discord
from discord.ext import commands
from discord import app_commands

# Grab token from Render environment
TOKEN = os.getenv("DISCORD_TOKEN")

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Bot setup
bot = commands.Bot(command_prefix="!", intents=intents)

# When bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"Slash sync failed: {e}")

# --- Moderation Commands ---

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason"):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} was kicked for: {reason}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason"):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} was banned for: {reason}")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Cleared {amount} messages.", delete_after=3)

# --- Utility Commands ---

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! Latency: `{round(bot.latency * 1000)}ms`")

@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"{member}'s Info", color=discord.Color.purple())
    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Joined", value=member.joined_at.strftime("%Y-%m-%d"))
    embed.set_thumbnail(url=member.avatar.url)
    await ctx.send(embed=embed)

# --- Fun Commands ---

@bot.command()
async def slap(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.mention} slapped {member.mention} 💥")

@bot.command()
async def rate(ctx, *, thing):
    import random
    await ctx.send(f"I rate `{thing}` a **{random.randint(1, 10)}/10**")

# --- Slash Commands ---

@bot.tree.command(name="hello", description="Say hi to bot")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention} 👋")

@bot.tree.command(name="ping", description="Latency check")
async def ping_slash(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! `{round(bot.latency * 1000)}ms`")

# --- Run Bot ---
bot.run(TOKEN)
