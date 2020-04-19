# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:13:50 2020

@author: Caec08
"""

import os
import discord
import asyncio
from dotenv import load_dotenv
from datetime import datetime

import logger

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


if __name__ == "__main__":
    
    # Get environment
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")

    # Connect to Discord
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
    
    