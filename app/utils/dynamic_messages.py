def stock_trend_string_symbol(stock_difference):
    stock_trend_string = ''
    if stock_difference == 0:
         stock_trend_string = "No change"
    elif stock_difference < 0:
         stock_trend_string = "📉"
    elif stock_difference > 0:
        stock_trend_string =  "📈"
    return stock_trend_string

def stock_string_package(index, vantage_stock, embed):
    stock_date =  vantage_stock.time_series_daily[index][0]
    stock_data = vantage_stock.time_series_daily[index][1]
    stock_difference = float(stock_data['4. close']) - float(stock_data['1. open'])
    stock_trend_string = stock_trend_string_symbol(stock_difference)
    embed.add_field(name="DATE", value=stock_date)
    embed.add_field(name="OPEN", value=stock_data['1. open'])
    embed.add_field(name="HIGH", value=stock_data["2. high"])
    embed.add_field(name="LOW", value=stock_data["3. low"])
    embed.add_field(name="CLOSE", value=stock_data["4. close"])
    embed.add_field(name="VOL", value=stock_data["5. volume"])
    embed.add_field(name="TREND", value=stock_trend_string)
    embed.add_field(name="\u200B", value="\u200B")
    embed.add_field(name="\u200B", value="\u200B")
    return embed

def stock_message(discord, vantage_stock):
   
    stock_information = vantage_stock.meta_data['1. Information']
    stock_symbol = f"{vantage_stock.meta_data['2. Symbol']}" 
    embed=discord.Embed(title=stock_symbol, description=stock_information, color=0x0080ff)
    embed = stock_string_package(0, vantage_stock, embed)
  
    return embed

def stock_list_message(discord, vantage_stock):
    stock_information = vantage_stock.meta_data['1. Information']
    stock_symbol = f"{vantage_stock.meta_data['2. Symbol']}" 
    embed=discord.Embed(title=stock_symbol, description=stock_information, color=0x0080ff)
    for i in range(0,3):
        embed = stock_string_package(i, vantage_stock, embed)
    
    return embed