import investpy
from investpy.search import search_events
import pandas as pd
import datetime

# df = investpy.get_stock_historical_data(stock='TFTSE',
#                                         country='united kingdom',
#                                         from_date='01/01/2019',
#                                         to_date='01/01/2020')

def get_series_ukx():
    dates = get_date()
    search_result = investpy.search_quotes(text='uk100', products=['indices'],
                                            countries=['united kingdom'], n_results=1)
    recent_data = search_result.retrieve_historical_data(from_date=dates[1], to_date=dates[0])
    # infomation = search_result.retrieve_information()
    # print(search_result)
    return recent_data

def get_date():
    now = datetime.datetime.now() - datetime.timedelta(days=1)
    now_dmy = "{0:%d/%m/%Y}".format(now)
    last_year_dmy = "{0:%d/%m/%Y}".format(now - datetime.timedelta(days=365))
    return now_dmy, last_year_dmy

if __name__ == "__main__":
    data = get_series_ukx()
    print(data.index)
    pass