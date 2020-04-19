# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:13:50 2020

@author: Caec08
"""

import os
import discord
import asyncio
import string
from dotenv import load_dotenv
from datetime import datetime

if __name__ == "__main__":
    
    print("Starting...")
    
    # Get environment
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")

    # Connect to Discord
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        content = message.content
        content = content.lower().strip()
        content = ' '.join(content.split())
        content = content.translate(str.maketrans("", "", string.punctuation))
        
        if content == "no u":
            try:
                await message.channel.send(f'@{message.author} No U')
            except:
                print("Could not reply")
    
    client.run(token)
