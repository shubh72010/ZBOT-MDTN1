from discord import app_commands

def register_commands(bot):
    @bot.tree.command(name="ping", description="Check if bot is alive")
    async def ping(interaction):
        await interaction.response.send_message("🏓 Pong!", ephemeral=True)

    @bot.tree.command(name="userinfo", description="Get user info")
    async def userinfo(interaction):
        user = interaction.user
        await interaction.response.send_message(f"User: {user.name}\nID: {user.id}")

    @bot.tree.command(name="serverinfo", description="Get server info")
    async def serverinfo(interaction):
        guild = interaction.guild
        await interaction.response.send_message(f"Server: {guild.name}\nMembers: {guild.member_count}")

    @bot.tree.command(name="say", description="Make the bot say something")
    @app_commands.describe(text="Text for bot to say")
    async def say(interaction, text: str):
        await interaction.response.send_message(text)

    @bot.tree.command(name="avatar", description="Get your profile picture")
    async def avatar(interaction):
        await interaction.response.send_message(interaction.user.avatar.url)

    @bot.tree.command(name="hello", description="Say hello")
    async def hello(interaction):
        await interaction.response.send_message(f"Hey {interaction.user.name}! 👋")

    # Add more commands as needed — same pattern

    # If needed, you can add per-server (guild) syncs:
    # await bot.tree.sync(guild=discord.Object(id=YOUR_TEST_SERVER_ID))