

import os

import discord
from dotenv import load_dotenv


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
            embed=discord.Embed(title="Welcome to the Yahoo Stock Bot!", description="Need help? Here are the commands!", color=0x0080ff)
            embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/information_2139.png")
            embed.add_field(name=help_cmd, value="Open this help menu again.", inline=False)
            embed.add_field(name=author_cmd, value="Who developed this bot? Find out with this command!", inline=False)
            await msgChannel.send(embed=embed)

        # Author command
        if msgContent.startswith(author_cmd):
            embed=discord.Embed(title="Author: Alex Canales", url="https://github.com/canaleal", description="Check out my GitHub for more projects!", color=0x0080ff)
            embed.add_field(name="Powered by:", value="Python & Google Cloud", inline=True)
            embed.set_footer(text="Let me know if you have any feedback! :)")
            await msgChannel.send(embed=embed)

        if message.content.startswith('$hello'):
            await message.channel.send('Hello. This is the bot!')

    client.run(TOKEN)
