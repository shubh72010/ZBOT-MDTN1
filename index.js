// index.js
import { Client, GatewayIntentBits, Events } from 'discord.js';
import dotenv from 'dotenv';
import commands from './cmds.js';

dotenv.config(); // loads .env

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.GuildMembers,
    GatewayIntentBits.MessageContent,
  ]
});

// Ready Event
client.once(Events.ClientReady, () => {
  console.log(`✅ ZBØT MDTN1 is online as ${client.user.tag}`);
});

// Slash Command Handler
client.on(Events.InteractionCreate, async (interaction) => {
  if (!interaction.isChatInputCommand()) return;

  const command = commands.find(cmd => cmd.name === interaction.commandName);
  if (!command) return;

  try {
    await command.execute(interaction);
  } catch (err) {
    console.error(err);
    await interaction.reply({ content: '❌ Error executing command.', ephemeral: true });
  }
});

// Login
client.login(process.env.TOKEN);

import express from 'express';
const app = express();
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});