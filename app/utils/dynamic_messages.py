from utils.date_time import get_date_yesterday_in_yyyy_mm_dd_format

def stock_message(discord, vantage_stock):
    date = get_date_yesterday_in_yyyy_mm_dd_format()

    stock_information = vantage_stock.meta_data['1. Information']
    stock_symbol = f"{vantage_stock.meta_data['2. Symbol']} ({vantage_stock.meta_data['3. Last Refreshed']})"
    stock_data = vantage_stock.time_series_daily[date]
    
    stock_open = stock_data['1. open']
    stock_close = stock_data['4. close']
    stock_difference = float(stock_close) - float(stock_open)
    stock_trend_string = ""
    if stock_difference == 0:
         stock_trend_string = "No change"
    elif stock_difference < 0:
         stock_trend_string = "📉"
    elif stock_difference > 0:
        stock_trend_string =  "📈"
        
    embed=discord.Embed(title=stock_symbol, description=stock_information, color=0x0080ff)
    embed.add_field(name="OPEN", value=stock_data['1. open'])
    embed.add_field(name="HIGH", value=stock_data["2. high"])
    embed.add_field(name="LOW", value=stock_data["3. low"])
    embed.add_field(name="CLOSE", value=stock_data["4. close"])
    embed.add_field(name="VOL", value=stock_data["5. volume"])
    embed.add_field(name="TREND", value=stock_trend_string)
  
    return embed

def stock_list_message(discord, vantage_stock):
    embed=discord.Embed(title="Stock List", description="Here is the list of stocks!", color=0x0080ff)
    embed.add_field(name="Symbol", value=vantage_stock.meta_data['2. Symbol'])
    return embed