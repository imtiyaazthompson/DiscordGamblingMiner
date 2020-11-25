import discord
import os
from dotenv import load_dotenv


# Retrieve set environment variables in a .env file
def read_bot_key():
    load_dotenv()
    return os.getenv("BOT_TOKEN")


# Client represents a connection to discord and handles events
def connect():
    return discord.Client()


gamble_miner = connect()

# Event handler on_ready
@gamble_miner.event
async def on_ready():
    print(f"{gamble_miner.user} has connected to Discord")


# Run the client then asynchronously run the on_ready event handler
# that handles when a connection to the discord has been made
gamble_miner.run(read_bot_key())
