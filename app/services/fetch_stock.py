import os
import requests
import json

from models.vantage_stock import VantageStock

class FetchStock:
    def __init__(self):
        self.url = os.getenv('VANTAGE_URL')
        self.closing_tag = "&interval=5min&apikey=" + os.getenv('VANTAGE_API_KEY')
        
    def get_stock_data(self, symbol):
        response = requests.get(self.url + symbol + self.closing_tag)
        data = json.loads(response.text)
        return VantageStock(data['Meta Data'], data['Time Series (Daily)'])