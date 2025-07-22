export default [
  {
    name: 'ping',
    description: 'Replies with Pong!',
    execute: async (interaction) => {
      await interaction.reply('🏓 Pong!');
    }
  }
];