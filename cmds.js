// Each command is an object with a name + execute function
export const commands = [
  {
    name: 'Say Hello',
    execute: () => {
      return '👋 Hello, user!';
    }
  },
  {
    name: 'Show Time',
    execute: () => {
      return `🕒 Current time: ${new Date().toLocaleTimeString()}`;
    }
  },
  {
    name: 'Random Number',
    execute: () => {
      return `🎲 Random number: ${Math.floor(Math.random() * 100)}`;
    }
  },
  {
    name: 'System Info',
    execute: () => {
      return `⚙️ User Agent: ${navigator.userAgent}`;
    }
  }
];