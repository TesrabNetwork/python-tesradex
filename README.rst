================================
Welcome to python-tesradex v0.1.11
================================

This is an unofficial Python wrapper for the `Tesradex exchanges REST API v1 <https://tesradexapidocs.docs.apiary.io/>`_. I am in no way affiliated with Tesradex, use at your own risk.

PyPi
  https://pypi.python.org/pypi/python-tesradex

Source code
  https://github.com/TesrabNetwork/python-tesradex

Documentation
  https://python-tesradex.readthedocs.io/en/latest/


Features
--------

- Implementation of most REST endpoints, more coming soon.
- Simple handling of authentication
- Response exception handling
- Simple buy and sell order functions
- Helper function `get_total_balance` to get balance in fiat
- Historical Kline/Candle fetching function `get_historical_klines_tv`

Quick Start
-----------

Register an account with `Tesradex <https://www.tesradex.com/#/?r=E42cWB>`_.

`Generate an API Key <https://www.tesradex.com/#/user/setting/api>`_ and enable it.

.. code:: bash

    pip install python-tesradex


.. code:: python

    from tesradex.client import Client
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


For more `check out the documentation <https://python-tesradex.readthedocs.io/en/latest/>`_.

Other Languages
---------------

If you use `Javascript <https://www.binance.com/?ref=10099792>`_ check out the `Javascript-Tesradex <https://github.com/sammchardy/python-binance>`_ library.

If you use `Java <https://www.allcoin.com/Account/RegisterByPhoneNumber/?InviteCode=MTQ2OTk4MDgwMDEzNDczMQ==>`_ check out the `Java-Tesradex <https://github.com/sammchardy/python-allcoin>`_ library.

If you use `PHP <https://accounts.quoinex.com/sign-up?affiliate=PAxghztC67615>`_
or `Qryptos <https://accounts.qryptos.com/sign-up?affiliate=PAxghztC67615>`_ check out the `PHP-Tesradex <https://github.com/sammchardy/python-quoine>`_ library.

If you use `Go <https://idex.market>`_ check out the `Go-Tesradex <https://github.com/sammchardy/python-idex>`_ library.

If you use `C/CPP <https://big.one>`_ check out the `C/CPP-Tesradex <https://github.com/sammchardy/python-bigone>`_ library.

.. image:: https://analytics-pixel.appspot.com/UA-111417213-1/github/python-tesradex?pixel
