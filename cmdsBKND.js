export default function(bot) {
  bot.on('messageCreate', async (msg) => {
    if (!msg.guild || msg.author.bot) return;

    if (msg.content.startsWith('!ban')) {
      if (!msg.member.permissions.has('BanMembers')) return msg.reply("❌ No perms.");
      const member = msg.mentions.members.first();
      if (!member) return msg.reply("Mention someone to ban.");
      try {
        await member.ban();
        msg.reply(`✅ Banned ${member.user.tag}`);
      } catch {
        msg.reply("Couldn't ban.");
      }
    }

    if (msg.content.startsWith('!kick')) {
      if (!msg.member.permissions.has('KickMembers')) return msg.reply("❌ No perms.");
      const member = msg.mentions.members.first();
      if (!member) return msg.reply("Mention someone to kick.");
      try {
        await member.kick();
        msg.reply(`✅ Kicked ${member.user.tag}`);
      } catch {
        msg.reply("Couldn't kick.");
      }
    }

    // More moderation cmds...
  });
}