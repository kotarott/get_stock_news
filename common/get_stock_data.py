import investpy
from investpy.search import search_events
import pandas as pd

# df = investpy.get_stock_historical_data(stock='TFTSE',
#                                         country='united kingdom',
#                                         from_date='01/01/2019',
#                                         to_date='01/01/2020')

search_result = investpy.search_quotes(text='uk100', products=['indices'],
                                       countries=['united kingdom'], n_results=1)
# recent_data = search_result.retrieve_historical_data(from_date='02/08/2021', to_date='27/08/2021')
infomation = search_result.retrieve_information()
# print(search_result)
print(infomation)