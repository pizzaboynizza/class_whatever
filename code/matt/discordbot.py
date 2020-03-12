# bot.py
import os
import discord
import random
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

# client = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')
    # guild = discord.utils.get(client.guilds, name=GUILD)

@bot.event # messages new users when they join the discord server.
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.event # ensures that if message originates from bot that it won't trigger additional onMessage() commands.
async def on_message(message):
    if message.author == bot.user:
        return
    elif message.content == 'raise-exception':
        raise discord.DiscordException


@bot.event # writes exceptions to err.log file for better troubleshooting.
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

    # print(
    #     f'{client.user} is connected to the following guild:\n'
    #     f'{guild.name}(id: {guild.id})'
    # )

    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')


# client.run(TOKEN)
bot.run(TOKEN)