from discord.ext import commands

# Example command
async def register_commands(bot: commands.Bot):
    @bot.command(name="ping")
    async def ping(ctx):
        await ctx.send("Pong!")

    @bot.command(name="say")
    async def say(ctx, *, message: str):
        await ctx.send(message)

    @bot.command(name="serverinfo")
    async def serverinfo(ctx):
        guild = ctx.guild
        await ctx.send(f"Server: {guild.name}\nMembers: {guild.member_count}")