// Example backend-like commands (requires actual endpoints to work)

export async function doPing() {
  try {
    const res = await fetch('https://your-api-url.com/ping'); // Replace with real URL
    if (!res.ok) throw new Error('Server responded with an error');
    
    const data = await res.json();
    return `✅ Server responded: ${data.message || 'pong'}`;
  } catch (err) {
    return `❌ Ping failed: ${err.message}`;
  }
}

export async function getServerStatus() {
  try {
    const res = await fetch('https://your-api-url.com/status'); // Replace with real URL
    const data = await res.json();
    return `🖥️ Status: ${data.status || 'Unknown'}`;
  } catch (err) {
    return `❌ Could not get server status: ${err.message}`;
  }
}

export async function sendBotMessage(channelId, content) {
  try {
    const res = await fetch('https://your-api-url.com/sendMessage', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ channelId, content })
    });

    if (!res.ok) throw new Error('Failed to send message');
    const data = await res.json();

    return `✅ Sent: ${data.status || 'Delivered'}`;
  } catch (err) {
    return `❌ Error sending message: ${err.message}`;
  }
}