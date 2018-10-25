Welcome to python-kucoin v0.1.11
          
This is an unofficial Python wrapper for the Kucoin exchanges REST API v1. I am in no way affiliated with Kucoin, use at your own risk.

PyPi
https://pypi.python.org/pypi/python-kucoin
Source code
https://github.com/sammchardy/python-kucoin
Documentation
https://python-kucoin.readthedocs.io/en/latest/
Blog with examples
https://sammchardy.github.io
Features
Implementation of most REST endpoints, more coming soon.
Simple handling of authentication
Response exception handling
Simple buy and sell order functions
Helper function get_total_balance to get balance in fiat
Historical Kline/Candle fetching function get_historical_klines_tv
Quick Start
Register an account with Kucoin.

Generate an API Key and enable it.

pip install python-kucoin
from kucoin.client import Client
client = Client(api_key, api_secret)

# get currencies
currencies = client.get_currencies()

# get market depth
depth = client.get_order_book('KCS-BTC', limit=50)

# get symbol klines
from_time = 1507479171
to_time = 1510278278
klines = client.get_kline_data_tv(
    'KCS-BTC',
    Client.RESOLUTION_1MINUTE,
    from_time,
    to_time
)

# place a buy order
transaction = client.create_buy_order('KCS-BTC', '0.01', '1000')

# get list of active orders
orders = client.get_active_orders('KCS-BTC')

# get historical kline data from any date range

# fetch 1 minute klines for the last day up until now
klines = client.get_historical_klines_tv("KCS-BTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

# fetch 30 minute klines for the last month of 2017
klines = client.get_historical_klines_tv("ETH-BTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")

# fetch weekly klines since it listed
klines = client.get_historical_klines_tv("NEO-BTC", KLINE_INTERVAL_1WEEK, "1 Jan, 2017")
For more check out the documentation.

Donate
If this library helped you out feel free to donate.

ETH: 0xD7a7fDdCfA687073d7cC93E9E51829a727f9fE70
NEO: AVJB4ZgN7VgSUtArCt94y7ZYT6d5NDfpBo
LTC: LPC5vw9ajR1YndE1hYVeo3kJ9LdHjcRCUZ
BTC: 1Dknp6L6oRZrHDECRedihPzx2sSfmvEBys
Other Exchanges
If you use Binance check out my python-binance library.

If you use Allcoin check out my python-allucoin library.

If you use Quoinex or Qryptos check out my python-quoine library.

If you use IDEX check out my python-idex library.

If you use BigONE check out my python-bigone library.

https://analytics-pixel.appspot.com/UA-111417213-1/github/python-kucoin?pixel
