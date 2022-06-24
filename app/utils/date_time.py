
import datetime

def get_date_in_yyyy_mm_dd_format():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def get_date_yesterday_in_yyyy_mm_dd_format():
    return (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")