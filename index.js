import express from 'express';
import { Client, GatewayIntentBits, Events } from 'discord.js';
import { config } from 'dotenv';
import cmds from './cmdsBKND.js';
import { commands } from './cmds.js';

// On interaction create:
client.on('interactionCreate', async interaction => {
  if (!interaction.isChatInputCommand()) return;

  const command = commands.find(cmd => cmd.data.name === interaction.commandName);
  if (!command) return;

  try {
    await command.execute(interaction);
  } catch (err) {
    console.error(err);
    await interaction.reply({ content: 'There was an error executing that command.', ephemeral: true });
  }
});

config();

const app = express();
const PORT = process.env.PORT || 3000;

// Discord client setup
const bot = new Client({
  intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent],
});

// Load commands
bot.on(Events.ClientReady, () => {
  console.log(`✅ Logged in as ${bot.user.tag}`);
  cmds(bot);
});

bot.login(process.env.BOT_TOKEN);

// Express simple route
app.get('/', (req, res) => {
  res.send('ZBØT MDTN1 Backend is Live 🚀');
});

app.listen(PORT, () => {
  console.log(`🌐 Web server up at http://localhost:${PORT}`);
});