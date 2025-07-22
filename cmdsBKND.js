export const commands = [
  {
    name: "ping",
    description: "Returns bot latency",
    async execute({ message }) {
      const sent = await message.channel.send("Pinging...");
      sent.edit(`🏓 Pong! Latency is ${sent.createdTimestamp - message.createdTimestamp}ms.`);
    },
  },
  {
    name: "say",
    description: "Echoes your input",
    async execute({ message, args }) {
      if (!args.length) return message.reply("You gotta say *something*!");
      message.channel.send(args.join(" "));
    },
  },
  {
    name: "kick",
    description: "Kicks a user",
    async execute({ message, args }) {
      if (!message.member.permissions.has("KICK_MEMBERS")) return message.reply("No perms.");
      const member = message.mentions.members.first();
      if (!member) return message.reply("Mention someone to kick!");
      await member.kick();
      message.channel.send(`${member.user.tag} got yeeted.`);
    },
  },
  {
    name: "ban",
    description: "Bans a user",
    async execute({ message, args }) {
      if (!message.member.permissions.has("BAN_MEMBERS")) return message.reply("No perms.");
      const member = message.mentions.members.first();
      if (!member) return message.reply("Mention someone to ban!");
      await member.ban();
      message.channel.send(`${member.user.tag} got obliterated.`);
    },
  },
  {
    name: "purge",
    description: "Deletes messages",
    async execute({ message, args }) {
      if (!message.member.permissions.has("MANAGE_MESSAGES")) return message.reply("No perms.");
      const amount = parseInt(args[0]);
      if (isNaN(amount) || amount < 1 || amount > 100) return message.reply("1-100 only.");
      await message.channel.bulkDelete(amount, true);
      message.channel.send(`Deleted ${amount} messages`).then(msg => setTimeout(() => msg.delete(), 2000));
    },
  },
  {
    name: "userinfo",
    description: "Shows user info",
    async execute({ message, args }) {
      const user = message.mentions.users.first() || message.author;
      message.channel.send(`👤 **User:** ${user.tag}\n🆔 **ID:** ${user.id}`);
    },
  },
  {
    name: "serverinfo",
    description: "Shows server info",
    async execute({ message }) {
      const { guild } = message;
      message.channel.send(`🌐 **Server:** ${guild.name}\n👥 **Members:** ${guild.memberCount}`);
    },
  },
  {
    name: "avatar",
    description: "Shows avatar",
    async execute({ message, args }) {
      const user = message.mentions.users.first() || message.author;
      message.channel.send({ content: `${user.displayAvatarURL({ dynamic: true, size: 512 })}` });
    },
  },
  {
    name: "reverse",
    description: "Reverses your text",
    async execute({ message, args }) {
      const text = args.join(" ");
      if (!text) return message.reply("Say something!");
      message.channel.send([...text].reverse().join(""));
    },
  },
  {
    name: "8ball",
    description: "Ask the magic 8-ball",
    async execute({ message, args }) {
      if (!args.length) return message.reply("Ask something.");
      const responses = ["Yes.", "No.", "Maybe.", "Definitely.", "Ask again later."];
      const reply = responses[Math.floor(Math.random() * responses.length)];
      message.reply(reply);
    },
  },
  {
    name: "calc",
    description: "Basic calculator",
    async execute({ message, args }) {
      try {
        const result = eval(args.join(" "));
        message.channel.send(`🧮 Result: ${result}`);
      } catch {
        message.reply("Invalid math expression.");
      }
    },
  },
  {
    name: "meme",
    description: "Sends a meme (placeholder)",
    async execute({ message }) {
      message.channel.send("😆 Here's a meme! (Imagine one here)");
    },
  },
  {
    name: "coinflip",
    description: "Flips a coin",
    async execute({ message }) {
      const result = Math.random() < 0.5 ? "Heads" : "Tails";
      message.channel.send(`🪙 ${result}`);
    },
  },
  {
    name: "dice",
    description: "Rolls a dice",
    async execute({ message }) {
      const roll = Math.floor(Math.random() * 6) + 1;
      message.channel.send(`🎲 You rolled a ${roll}`);
    },
  },
  {
    name: "mock",
    description: "Mocks your text",
    async execute({ message, args }) {
      const text = args.join(" ");
      const mocked = text
        .split("")
        .map((char, i) => (i % 2 ? char.toUpperCase() : char.toLowerCase()))
        .join("");
      message.channel.send(mocked);
    },
  },
  {
    name: "uptime",
    description: "Bot uptime",
    async execute({ message }) {
      const seconds = Math.floor(process.uptime());
      const minutes = Math.floor(seconds / 60);
      const hours = Math.floor(minutes / 60);
      message.channel.send(`⏱ Uptime: ${hours}h ${minutes % 60}m ${seconds % 60}s`);
    },
  },
  {
    name: "time",
    description: "Shows current time",
    async execute({ message }) {
      const now = new Date();
      message.channel.send(`🕒 Current time: ${now.toUTCString()}`);
    },
  },
  {
    name: "joke",
    description: "Tells a joke",
    async execute({ message }) {
      const jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you get when you cross a snowman and a vampire? Frostbite."
      ];
      message.channel.send(jokes[Math.floor(Math.random() * jokes.length)]);
    },
  },
  {
    name: "quote",
    description: "Random motivational quote",
    async execute({ message }) {
      const quotes = [
        "Believe in yourself.",
        "You got this.",
        "The future is now.",
        "Push through the chaos."
      ];
      message.channel.send(quotes[Math.floor(Math.random() * quotes.length)]);
    },
  },
  {
    name: "help",
    description: "Lists all commands",
    async execute({ message }) {
      message.channel.send("Type any of the following: `ping`, `say`, `kick`, `ban`, `purge`, `userinfo`, `serverinfo`, `avatar`, `reverse`, `8ball`, `calc`, `coinflip`, `mock`, `meme`, `uptime`, `time`, `joke`, `quote`, etc.");
    },
  },
  // Add 10 more similar basic ones as placeholders
  ...Array.from({ length: 10 }, (_, i) => ({
    name: `custom${i + 1}`,
    description: `Placeholder command ${i + 1}`,
    async execute({ message }) {
      message.channel.send(`🛠️ This is custom command ${i + 1}`);
    },
  }))
];