
def help_message(discord):
    embed=discord.Embed(title="Help", description="This is the help message!", color=0x0080ff)
    embed.add_field(name="$ping", value="Shows network ping", inline=True)
    embed.add_field(name="$help", value="Shows this message", inline=True)
    embed.add_field(name="$author", value="Shows the author", inline=True)
    embed.set_footer(text="Let me know if you have any feedback! :)")
    return embed

def author_message(discord):
    embed=discord.Embed(title="Author: Alex Canales", url="https://github.com/canaleal", description="Check out my GitHub for more projects!", color=0x0080ff)
    embed.add_field(name="Powered by:", value="Python & Google Cloud", inline=True)
    embed.set_footer(text="Let me know if you have any feedback! :)")
    return embed