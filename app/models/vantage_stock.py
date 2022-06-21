
class VantageStock:
    def __init__ (self, meta_data, time_series):
        self.meta_data = meta_data
        self.time_series = time_series
        
    def get_meta_data(self):
        return self.meta_data
    
    
    def get_all_time_series(self):
        return self.time_series
    
    def get_first_time_series_string(self):
        first_element = list(self.time_series)[0]
        return str(first_element)