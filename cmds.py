import discord
from discord import app_commands
from discord.ext import commands
import random
import datetime
import asyncio
import platform
import psutil
import os

class BasicCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Shows bot latency")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong! 🏓 `{round(self.bot.latency * 1000)}ms`")

    @app_commands.command(name="userinfo", description="Shows info about a user")
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member = None):
        member = member or interaction.user
        embed = discord.Embed(title="User Info", color=discord.Color.blurple())
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.add_field(name="Username", value=member.name, inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Created", value=member.created_at.strftime("%Y-%m-%d"), inline=True)
        embed.add_field(name="Joined", value=member.joined_at.strftime("%Y-%m-%d") if member.joined_at else "N/A", inline=True)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="serverinfo", description="Shows info about this server")
    async def serverinfo(self, interaction: discord.Interaction):
        guild = interaction.guild
        embed = discord.Embed(title=guild.name, description="Server Information", color=discord.Color.green())
        embed.set_thumbnail(url=guild.icon.url if guild.icon else "")
        embed.add_field(name="Owner", value=str(guild.owner), inline=True)
        embed.add_field(name="Members", value=guild.member_count, inline=True)
        embed.add_field(name="Created", value=guild.created_at.strftime("%Y-%m-%d"), inline=True)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="say", description="Make the bot say something")
    async def say(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(message)

    @app_commands.command(name="random", description="Pick a random number")
    async def random_num(self, interaction: discord.Interaction, start: int, end: int):
        if start > end:
            await interaction.response.send_message("Invalid range!", ephemeral=True)
        else:
            num = random.randint(start, end)
            await interaction.response.send_message(f"🎲 Your number: `{num}`")

    @app_commands.command(name="8ball", description="Ask the magic 8ball a question")
    async def eightball(self, interaction: discord.Interaction, question: str):
        responses = [
            "Yes.", "No.", "Maybe.", "Definitely.", "Not sure.", "Ask again later.",
            "Absolutely!", "I wouldn’t count on it.", "You bet.", "Doubt it."
        ]
        await interaction.response.send_message(f"🎱 **Question:** {question}\n**Answer:** {random.choice(responses)}")

    @app_commands.command(name="flip", description="Flip a coin")
    async def flip(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"🪙 You got: `{random.choice(['Heads', 'Tails'])}`")

    @app_commands.command(name="roll", description="Roll a die")
    async def roll(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"🎲 You rolled: `{random.randint(1, 6)}`")

    @app_commands.command(name="uptime", description="Bot uptime")
    async def uptime(self, interaction: discord.Interaction):
        now = datetime.datetime.utcnow()
        delta = now - self.bot.launch_time
        await interaction.response.send_message(f"⏱ Uptime: `{str(delta).split('.')[0]}`")

    @app_commands.command(name="botinfo", description="Bot system info")
    async def botinfo(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Bot Info", color=discord.Color.dark_teal())
        embed.add_field(name="Python", value=platform.python_version(), inline=True)
        embed.add_field(name="RAM Usage", value=f"{psutil.Process().memory_info().rss / 1024 ** 2:.2f} MB", inline=True)
        embed.add_field(name="Platform", value=platform.system(), inline=True)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="clear", description="Clear messages (admin only)")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clear(self, interaction: discord.Interaction, amount: int):
        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"🧹 Cleared `{amount}` messages!", ephemeral=True)

    @app_commands.command(name="ban", description="Ban a member (admin only)")
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        await member.ban(reason=reason)
        await interaction.response.send_message(f"🔨 Banned {member}!")

    @app_commands.command(name="kick", description="Kick a member (admin only)")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        await member.kick(reason=reason)
        await interaction.response.send_message(f"👢 Kicked {member}!")

    @app_commands.command(name="poll", description="Create a poll")
    async def poll(self, interaction: discord.Interaction, question: str, option1: str, option2: str):
        embed = discord.Embed(title="📊 Poll", description=question, color=discord.Color.purple())
        embed.add_field(name="1️⃣", value=option1, inline=True)
        embed.add_field(name="2️⃣", value=option2, inline=True)
        msg = await interaction.channel.send(embed=embed)
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        await interaction.response.send_message("Poll created!", ephemeral=True)

    @app_commands.command(name="remind", description="Set a reminder")
    async def remind(self, interaction: discord.Interaction, minutes: int, reminder: str):
        await interaction.response.send_message(f"⏰ I will remind you in {minutes} minutes.")
        await asyncio.sleep(minutes * 60)
        await interaction.followup.send(f"🔔 Reminder: {reminder}")

async def setup(bot: commands.Bot):
    await bot.add_cog(BasicCommands(bot))