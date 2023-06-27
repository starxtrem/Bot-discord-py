# Discord Bot Readme

This code represents a Discord bot that utilizes the Discord.py library. The bot has several features, including displaying the bot's latency, providing a help command, and updating the player count for a game server.

## Prerequisites

Before running the code, make sure you have the following:

- Python installed on your system.
- Required packages installed. You can install them using pip:

```bash
pip install discord
pip install python-dotenv
```

## Setup

1. Create a new Discord application and bot on the [Discord Developer Portal](https://discord.com/developers/applications).
2. Copy the bot token and replace `discord_tokenbot` in the code with your bot token.
3. If necessary, adjust the `configipserv` variable with the appropriate server IP.
4. Create a `.env` file in the same directory as the code and add the following lines:

```
discord_tokenbot=YOUR_BOT_TOKEN
configipserv=YOUR_SERVER_IP
```

## Running the Bot

To run the Discord bot, execute the Python script:
```
python bot.py
```

## Commands

The bot provides the following commands:

- **/ping**: Returns the bot's latency in milliseconds.
- **/help**: Displays a list of available commands.

## Event Handlers

The bot also includes event handlers for certain Discord events:

- **on_ready**: Triggered when the bot successfully connects to Discord. It prints the bot's information and syncs commands.
- **on_guild_join**: Triggered when the bot joins a new guild (server). It prints the updated server count.
- **on_guild_remove**: Triggered when the bot is removed from a guild. It prints the updated server count.

## Update Player Count

The bot includes a task loop that updates the player count every 10 seconds. It fetches the player data from the specified server IP and updates the bot's presence with the player count. If an error occurs, it displays "Error getting player count" and sets the presence to "Server offline."

## Additional Notes

- This bot is designed to be sharded, meaning it can distribute its workload across multiple instances for larger servers.
- The bot removes the default help command to replace it with a custom implementation.

Feel free to modify and extend this code to suit your specific needs.
