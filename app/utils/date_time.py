
import datetime

def get_date_in_yyyy_mm_dd_format():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def get_date_yesterday_n_days(days_back):
    return (datetime.datetime.now() - datetime.timedelta(days=days_back)).strftime("%Y-%m-%d")

def get_date_yesterday_in_yyyy_mm_dd_format():
    return get_date_yesterday_n_days(1)

def get_last_three_dates_in_array_yyyy_mm_dd_format():
    list_days = []
    for i in range(1,4):
        list_days.append(get_date_yesterday_n_days(i))
    return list_days
