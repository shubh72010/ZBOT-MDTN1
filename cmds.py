from discord import app_commands, Interaction
import random
import datetime
import platform
import os

async def setup_commands(bot):
    @bot.tree.command(name="ping", description="Check bot latency.")
    async def ping(interaction: Interaction):
        await interaction.response.send_message(f"Pong! `{round(bot.latency * 1000)}ms`")

    @bot.tree.command(name="roll", description="Roll a dice.")
    async def roll(interaction: Interaction):
        value = random.randint(1, 6)
        await interaction.response.send_message(f"You rolled a 🎲 `{value}`")

    @bot.tree.command(name="userinfo", description="Get your Discord info.")
    async def userinfo(interaction: Interaction):
        user = interaction.user
        await interaction.response.send_message(f"Username: `{user}`\nID: `{user.id}`")

    @bot.tree.command(name="serverinfo", description="Details about this server.")
    async def serverinfo(interaction: Interaction):
        guild = interaction.guild
        embed = discord.Embed(title=f"{guild.name} Info", color=discord.Color.blurple())
        embed.add_field(name="ID", value=guild.id)
        embed.add_field(name="Members", value=guild.member_count)
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        await interaction.response.send_message(embed=embed)

    @bot.tree.command(name="botinfo", description="Details about this bot.")
    async def botinfo(interaction: Interaction):
        embed = discord.Embed(title="Bot Info", color=discord.Color.green())
        embed.add_field(name="Python", value=platform.python_version())
        embed.add_field(name="Library", value="discord.py")
        embed.add_field(name="OS", value=platform.system())
        await interaction.response.send_message(embed=embed)

    @bot.tree.command(name="say", description="Make the bot say something.")
    @app_commands.describe(text="The message you want the bot to say")
    async def say(interaction: Interaction, text: str):
        await interaction.response.send_message(text)

    @bot.tree.command(name="coinflip", description="Flip a coin.")
    async def coinflip(interaction: Interaction):
        result = random.choice(["Heads", "Tails"])
        await interaction.response.send_message(f"The coin landed on **{result}**.")

    @bot.tree.command(name="choose", description="Let the bot pick between choices.")
    @app_commands.describe(options="Comma-separated options to choose from")
    async def choose(interaction: Interaction, options: str):
        choices = [opt.strip() for opt in options.split(",") if opt.strip()]
        if not choices:
            await interaction.response.send_message("No valid choices provided.")
        else:
            choice = random.choice(choices)
            await interaction.response.send_message(f"I choose: **{choice}**")

    @bot.tree.command(name="time", description="Show current server time.")
    async def time(interaction: Interaction):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await interaction.response.send_message(f"🕒 Current server time: `{now}`")

    @bot.tree.command(name="env", description="List available environment vars.")
    async def env(interaction: Interaction):
        vars = ", ".join(os.environ.keys())
        await interaction.response.send_message(f"Environment Variables: `{vars}`")

    # Add more below as needed...