from discord import app_commands, Interaction
import discord
import random
import datetime

def register_commands(bot):
    @bot.tree.command(name="ping", description="🏓 Check bot latency")
    async def ping(interaction: Interaction):
        await interaction.response.send_message(f"Pong! `{round(bot.latency*1000)}ms`")

    @bot.tree.command(name="echo", description="Echo back your input")
    async def echo(interaction: Interaction, message: str):
        await interaction.response.send_message(message)

    @bot.tree.command(name="roll", description="Roll a dice (1-100)")
    async def roll(interaction: Interaction):
        v = random.randint(1, 100)
        await interaction.response.send_message(f"🎲 You got **{v}**")

    @bot.tree.command(name="time", description="Show current server time")
    async def time(interaction: Interaction):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await interaction.response.send_message(f"🕒 {now}")

    @bot.tree.command(name="userinfo", description="Your Discord user info")
    async def userinfo(interaction: Interaction):
        u = interaction.user
        await interaction.response.send_message(
            f"👤 User: {u}\n🆔 ID: {u.id}\n📅 Joined Discord: {u.created_at.strftime('%Y-%m-%d')}"
        )

    @bot.tree.command(name="sayhi", description="Bot says hi to you")
    async def sayhi(interaction: Interaction):
        await interaction.response.send_message(f"Hello, {interaction.user.mention}! 👋")

    @bot.tree.command(name="coinflip", description="Flip a coin")
    async def coinflip(interaction: Interaction):
        result = random.choice(["Heads 🪙", "Tails 🪙"])
        await interaction.response.send_message(result)

    @bot.tree.command(name="choose", description="Pick from comma-separated list")
    async def choose(interaction: Interaction, options: str):
        choices = [opt.strip() for opt in options.split(",") if opt.strip()]
        if not choices:
            return await interaction.response.send_message("❌ Provide at least two options separated by commas.")
        pick = random.choice(choices)
        await interaction.response.send_message(f"I pick: **{pick}**")

    # Add more commands here...