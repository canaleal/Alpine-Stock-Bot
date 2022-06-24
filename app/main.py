

import os

import discord
from dotenv import load_dotenv
from utils import static_messages, dynamic_messages, filter_string
from services import fetch_stock


def get_stock(userMsg):
    stock_symbol = userMsg.upper()
    fetch_object = fetch_stock.FetchStock()
    stock = fetch_object.get_stock_data(stock_symbol)
    return stock


if __name__ == "__main__":

    prefix = "$"
    ping_cmd = prefix + "ping"
    stockCmd = prefix + "stock"
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

        if msgContent.startswith(ping_cmd):
            await msgChannel.send("Ping: {}ms".format(round(client.latency * 1000)))
            
        elif msgContent.startswith(stockCmd):
            userMsg = filter_string.get_second_word_from_string(msgContent)
            if len(userMsg) > 1:
               
                stock = get_stock(userMsg)    
                if isinstance(stock, str):
                    await msgChannel.send(stock)
                else: 
                    embed = dynamic_messages.stock_list_message(discord, stock) if msgContent.endswith("list") else dynamic_messages.stock_message(discord, stock) 
                    await msgChannel.send(embed=embed)
            else:
                await msgChannel.send("Please enter a stock symbol!\nExample: `{} CTS.TO`".format(stockCmd))
  
        # Help command
        elif msgContent.startswith(help_cmd):
            embed = static_messages.help_message(discord)
            await msgChannel.send(embed=embed)

        # Author command
        elif msgContent.startswith(author_cmd):
            embed = static_messages.author_message(discord)
            await msgChannel.send(embed=embed)

        elif message.content.startswith('$hello'):
            await message.channel.send('Hello. This is the bot!')

    client.run(TOKEN)
