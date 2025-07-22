import { commands } from './cmds.js';

document.addEventListener('DOMContentLoaded', () => {
  const cmdList = document.getElementById('command-list');
  const outputBox = document.getElementById('output');

  // Load all commands into UI
  commands.forEach(cmd => {
    const btn = document.createElement('button');
    btn.textContent = cmd.name;
    btn.className = 'cmd-btn glass';
    btn.onclick = () => {
      const result = cmd.execute();
      outputBox.textContent = result || `${cmd.name} executed!`;
    };
    cmdList.appendChild(btn);
  });
});