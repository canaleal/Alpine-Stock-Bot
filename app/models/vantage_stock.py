
class VantageStock:
    def __init__ (self, meta_data, time_series_daily):
        self.meta_data = meta_data
        self.time_series_daily = list(time_series_daily.items())
        
    def get_meta_data(self):
        return self.meta_data
    
    
    def get_all_time_daily_series(self):
        return self.time_series_daily
    
    def get_first_time_series_string(self):
        first_element = list(self.time_series_daily)[0]
        return str(first_element)