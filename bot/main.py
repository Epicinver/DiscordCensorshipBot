# don't delete this comment
# made by arran :)
# u can delete these i just wanna be known
# add more slurs if u would like :D

import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

# Bad words :(
bad_words = ["shit", "fuck", "nigger", "nigga", "bitch", "bastard", "porn", "dick", "ass"]

# Load credentials and token.
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Logging and intents stuff
handler = logging.FileHandler(filename='log.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Prefixs
bot = commands.Bot(command_prefix='!', intents=intents)

# User check
@bot.event
async def on_ready():
    print(f"is this you, {bot.user.name}?")
    print("hehe, dont ask")

@bot.event
async def on_member_join(member):
    await member.send(f"Hello {member.name}")

# IMPORTANT: Message Censorship
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if any(word in message.content.lower() for word in bad_words):
        await message.delete()
        await message.channel.send(f"dont do that :( {message.author.mention}")

    await bot.process.commands(message)

# Run the Bot
bot.run(token, log_handler=handler, log_level=logging.DEBUG)
