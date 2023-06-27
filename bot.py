import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import requests

load_dotenv()

discord_token = os.getenv("discord_tokenbot")
configip = os.getenv("configipserv")

intents = discord.Intents.all()
intents.members = True
client = commands.AutoShardedBot(command_prefix='/', intents=intents)
client.remove_command('help')
last_status = None

@client.event
async def on_ready():
    update_player_count.start()
    if client.shard_ids is None:
        print('We have logged in as {0.user} on {1} servers'.format(client, len(client.guilds)))
    else:
        shard_count = len(client.shard_ids)
        total_servers = sum(len(guilds) for guilds in client.guilds)
        print('We have logged in as {0.user} on {1} servers across {2} shards'.format(client, total_servers, shard_count))
    try:
        sync = await client.tree.sync()
        print(f"Synced {sync} commands")
    except Exception as e:
        print(f"Failed to sync commands: {e}")
        

@client.event
async def on_guild_join(guild):
    if client.shard_ids is None:
        print('We have logged in as {0.user} on {1} servers'.format(client, len(client.guilds)))
    else:
        shard_count = len(client.shard_ids)
        total_servers = sum(len(guilds) for guilds in client.guilds)
        print('We have logged in as {0.user} on {1} servers across {2} shards'.format(client, total_servers, shard_count))

@client.event
async def on_guild_remove(guild):
    if client.shard_ids is None:
        print('We have logged in as {0.user} on {1} servers'.format(client, len(client.guilds)))
    else:
        shard_count = len(client.shard_ids)
        total_servers = sum(len(guilds) for guilds in client.guilds)
        print('We have logged in as {0.user} on {1} servers across {2} shards'.format(client, total_servers, shard_count))

@client.tree.command(name="ping", description="Returns the bot's latency")
async def ping(ctx):
    if ctx.guild is None:
        return await ctx.response.send_message("You must use this command in a server")
    else:
        ping = round(client.latency * 100, 2)
        embed = discord.Embed(title="Ping", description=f"Latency: {ping}ms", color=0x6fa8dc)
        await ctx.response.send_message(embed=embed)

@client.tree.command(name="help", description="Returns the bot's commands")
async def help(ctx):
    if ctx.guild is None:
        return await ctx.response.send_message("You must use this command in a server")
    else:
        embed = discord.Embed(title="Help", description="Here are the commands for the bot", color=0x6fa8dc)
        embed.add_field(name="/ping", value="Returns the bot's latency", inline=False)
        embed.add_field(name="/help", value="Returns the bot's commands", inline=False)
        await ctx.response.send_message(embed=embed)


@tasks.loop(seconds=10)  # Mettez à jour toutes les 10 secondes (ajustez selon vos besoins)
async def update_player_count():
    url = configip
    try:
        response = requests.get(url)
        players = response.json()
        player_count = len(players)
        await client.change_presence(activity=discord.Game(name=f"Players : {player_count}"))
    except:
        print('Error getting player count')
        await client.change_presence(activity=discord.Game(name=f"Serveur offline"))

@update_player_count.before_loop
async def before_update_player_count():
    await client.wait_until_ready()

client.run(discord_token)