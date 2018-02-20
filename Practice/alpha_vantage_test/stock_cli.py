# https://github.com/RomelTorres/alpha_vantage
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
ts = TimeSeries(key='Y3086XYRBVO5KMFD', output_format='pandas')
data, meta_data = ts.get_intraday('AAPL', interval='1min', outputsize='full')
pprint(data.head(5))