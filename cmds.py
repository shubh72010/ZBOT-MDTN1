from discord.ext import commands

async def setup_commands(bot):

    @bot.command()
    async def ping(ctx):
        await ctx.send(f"Pong! 🏓 Latency: {round(bot.latency * 1000)}ms")

    @bot.command()
    async def say(ctx, *, msg):
        await ctx.send(msg)

    @bot.command()
    async def echo(ctx, *, text):
        await ctx.send(f"🗣️ {text}")

    @bot.command()
    async def clear(ctx, amount: int = 5):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"🧹 Cleared {amount} messages.", delete_after=2)

    @bot.command()
    async def avatar(ctx, member: commands.MemberConverter = None):
        member = member or ctx.author
        await ctx.send(member.avatar.url)

    @bot.command()
    async def userinfo(ctx, member: commands.MemberConverter = None):
        member = member or ctx.author
        embed = discord.Embed(title="User Info", color=discord.Color.blurple())
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="Name", value=member.name)
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Joined", value=member.joined_at)
        embed.add_field(name="Created", value=member.created_at)
        await ctx.send(embed=embed)

    @bot.command()
    async def serverinfo(ctx):
        guild = ctx.guild
        embed = discord.Embed(title="Server Info", color=discord.Color.green())
        embed.set_thumbnail(url=guild.icon.url)
        embed.add_field(name="Name", value=guild.name)
        embed.add_field(name="Owner", value=guild.owner)
        embed.add_field(name="Members", value=guild.member_count)
        embed.add_field(name="Created", value=guild.created_at)
        await ctx.send(embed=embed)

    @bot.command()
    async def dm(ctx, member: commands.MemberConverter, *, msg):
        try:
            await member.send(msg)
            await ctx.send("📨 DM sent.")
        except:
            await ctx.send("Failed to DM.")

    @bot.command()
    async def coinflip(ctx):
        import random
        await ctx.send("🪙 Heads!" if random.choice([True, False]) else "🪙 Tails!")

    @bot.command()
    async def roll(ctx, dice: str = "1d6"):
        import random
        try:
            rolls, limit = map(int, dice.lower().split("d"))
        except:
            return await ctx.send("Format has to be NdN (e.g. 2d6)")

        result = ", ".join(str(random.randint(1, limit)) for _ in range(rolls))
        await ctx.send(f"🎲 {result}")

    @bot.command()
    async def reverse(ctx, *, text):
        await ctx.send(text[::-1])

    @bot.command()
    async def joke(ctx):
        import requests
        res = requests.get("https://v2.jokeapi.dev/joke/Any?format=txt")
        if res.ok:
            await ctx.send(res.text)
        else:
            await ctx.send("No jokes for now 😞")

    @bot.command()
    async def uptime(ctx):
        import datetime
        now = datetime.datetime.utcnow()
        delta = now - bot.launch_time
        await ctx.send(f"⏱️ Uptime: {delta}")

    @bot.command()
    async def repeat(ctx, times: int, *, message):
        times = min(times, 5)
        for _ in range(times):
            await ctx.send(message)

    @bot.command()
    async def whoami(ctx):
        await ctx.send(f"You are {ctx.author.mention}!")

    @bot.command()
    async def serverowner(ctx):
        await ctx.send(f"Server Owner: {ctx.guild.owner}")

    @bot.command()
    async def emoji(ctx):
        await ctx.send("😎🔥💀🧠")

    @bot.command()
    async def ban(ctx, member: commands.MemberConverter, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention} ✅")

    @bot.command()
    async def unban(ctx, *, user):
        banned = await ctx.guild.bans()
        name, discrim = user.split("#")
        for ban_entry in banned:
            if ban_entry.user.name == name and ban_entry.user.discriminator == discrim:
                await ctx.guild.unban(ban_entry.user)
                await ctx.send(f"Unbanned {user} ✅")
                return
        await ctx.send("User not found.")

    @bot.command()
    async def mute(ctx, member: commands.MemberConverter):
        mute_role = await ctx.guild.create_role(name="Muted")
        for channel in ctx.guild.channels:
            await channel.set_permissions(mute_role, speak=False, send_messages=False)
        await member.add_roles(mute_role)
        await ctx.send(f"{member.mention} has been muted.")

    @bot.command()
    async def unmute(ctx, member: commands.MemberConverter):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if role:
            await member.remove_roles(role)
            await ctx.send(f"{member.mention} has been unmuted.")

    @bot.command()
    async def poll(ctx, *, question):
        msg = await ctx.send(f"📊 {question}")
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")

    @bot.command()
    async def nickname(ctx, member: commands.MemberConverter, *, new_name):
        await member.edit(nick=new_name)
        await ctx.send(f"Changed nickname to {new_name}")

    @bot.command()
    async def math(ctx, *, expr):
        try:
            result = eval(expr)
            await ctx.send(f"🧮 Result: `{result}`")
        except:
            await ctx.send("Invalid expression.")

    @bot.command()
    async def source(ctx):
        await ctx.send("GitHub soon™️")

    @bot.command()
    async def invite(ctx):
        await ctx.send("🔗 Invite coming soon.")

    @bot.command()
    async def sus(ctx):
        await ctx.send("ඞ")

    # Add more dumb/funny ones later 💀