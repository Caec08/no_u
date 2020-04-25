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
        content = content.translate(str.maketrans(string.punctuation, " "*len(string.punctuation)))
        content = ' '.join(content.split())
        
        s = content.split()
        
        for i in range(0,len(s)):
            if s[i] == "no":
                if s[i+1] == "u":
                    try:
                        await message.channel.send(f'{message.author.mention} No u')
                        return
                    except:
                        print("Could not reply")

    client.run(token)
