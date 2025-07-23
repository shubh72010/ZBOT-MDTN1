from discord import app_commands, Interaction
import discord
import random
import datetime

async def setup_commands(bot):
    @bot.tree.command(name="ping", description="Ping the bot")
    async def ping(interaction: Interaction):
        await interaction.response.send_message(f"Pong! `{round(bot.latency * 1000)}ms`")

    @bot.tree.command(name="roll", description="Roll a dice")
    async def roll(interaction: Interaction):
        value = random.randint(1, 6)
        await interaction.response.send_message(f"🎲 You rolled a `{value}`")

    @bot.tree.command(name="userinfo", description="See your user info")
    async def userinfo(interaction: Interaction):
        user = interaction.user
        await interaction.response.send_message(f"👤 Username: `{user}`\n🆔 ID: `{user.id}`")

    @bot.tree.command(name="say", description="Make the bot say something")
    @app_commands.describe(text="What should I say?")
    async def say(interaction: Interaction, text: str):
        await interaction.response.send_message(text)

    @bot.tree.command(name="time", description="Show the current time")
    async def time(interaction: Interaction):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await interaction.response.send_message(f"🕒 Server time: `{now}`")

    @bot.tree.command(name="coinflip", description="Flip a coin")
    async def coinflip(interaction: Interaction):
        result = random.choice(["Heads", "Tails"])
        await interaction.response.send_message(f"🪙 It's **{result}**!")

    @bot.tree.command(name="choose", description="Choose randomly from a list")
    @app_commands.describe(options="Separate options with commas")
    async def choose(interaction: Interaction, options: str):
        choices = [opt.strip() for opt in options.split(",") if opt.strip()]
        if not choices:
            await interaction.response.send_message("❌ You need to give me at least one valid option.")
        else:
            result = random.choice(choices)
            await interaction.response.send_message(f"I pick: **{result}**")