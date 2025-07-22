// cmds.js

export const commands = [
  {
    name: "kick",
    description: "Kick a member from the server",
    options: [
      {
        name: "user",
        type: 6, // USER
        description: "User to kick",
        required: true
      },
      {
        name: "reason",
        type: 3, // STRING
        description: "Reason for kicking",
        required: false
      }
    ]
  },
  {
    name: "ban",
    description: "Ban a member from the server",
    options: [
      {
        name: "user",
        type: 6,
        description: "User to ban",
        required: true
      },
      {
        name: "reason",
        type: 3,
        description: "Reason for ban",
        required: false
      }
    ]
  },
  {
    name: "mute",
    description: "Temporarily mute a member",
    options: [
      {
        name: "user",
        type: 6,
        description: "User to mute",
        required: true
      },
      {
        name: "duration",
        type: 3,
        description: "Mute duration (e.g., 10m, 1h)",
        required: true
      }
    ]
  },
  {
    name: "warn",
    description: "Warn a member",
    options: [
      {
        name: "user",
        type: 6,
        description: "User to warn",
        required: true
      },
      {
        name: "reason",
        type: 3,
        description: "Reason for warning",
        required: false
      }
    ]
  }
];

export default commands;