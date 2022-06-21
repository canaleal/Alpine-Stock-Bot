

import os

import discord
from dotenv import load_dotenv
from utils import static_messages


if __name__ == "__main__":
    
    prefix = "$"
    help_cmd = prefix + "help"
    author_cmd = prefix + "author"
    
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')
    
    client = discord.Client()
    

    @client.event
    async def on_ready():
        for guild in client.guilds:
            print(
                f'{client.user} is connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})'
            )
            
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        msgContent = message.content
        msgChannel = message.channel
        
        # Help command
        if msgContent.startswith(help_cmd):
            embed = static_messages.help_message(discord)
            await msgChannel.send(embed=embed)

        # Author command
        if msgContent.startswith(author_cmd):
            embed = static_messages.author_message(discord)
            await msgChannel.send(embed=embed)

        if message.content.startswith('$hello'):
            await message.channel.send('Hello. This is the bot!')

    client.run(TOKEN)
