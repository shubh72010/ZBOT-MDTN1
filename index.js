import express from 'express';
import { Client, GatewayIntentBits, Events } from 'discord.js';
import { config } from 'dotenv';
import cmds from './cmdsBKND.js';

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