================================
Welcome to python-tesradex v1.0.0
================================

This is an unofficial Python wrapper for the `Tesradex exchanges REST API v1 <https://tesradexapidocs.docs.apiary.io/>`_. Use at your own risk.

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

Register an account with `Tesradex <https://www.tesrabnetwrok.com/tesradex`_.

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
        'TDEX-BTC',
        Client.RESOLUTION_1MINUTE,
        from_time,
        to_time
    )

    # place a buy order
    transaction = client.create_buy_order('TDEX-BTC', '0.01', '1000')

    # get list of active orders
    orders = client.get_active_orders('TDEX-BTC')

    # get historical kline data from any date range

    # fetch 1 minute klines for the last day up until now
    klines = client.get_historical_klines_tv("TDEX-BTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

    # fetch 30 minute klines for the last month of 2017
    klines = client.get_historical_klines_tv("ETH-BTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")

    # fetch weekly klines since it listed
    klines = client.get_historical_klines_tv("NEO-BTC", KLINE_INTERVAL_1WEEK, "1 Jan, 2017")


For more `check out the documentation <https://python-tesradex.readthedocs.io/en/latest/>`_.

Other Languages
---------------

If you use `Javascript <https://www.javascript.com/>`_ check out the `Javascript-Tesradex <https://github.com/TesrabNetwork/Javascript-Tesradex>`_ library.

If you use `Java <https://www.oracle.com/java/>`_ check out the `Java-Tesradex <https://github.com/TesrabNetwork/Java-Tesradex>`_ library.

If you use `C <https://www.cprogramming.com/tutorial/c-tutorial.html`_
or `CPP <https://www.cprogramming.com/tutorial/c++-tutorial.html>`_ check out the `C/CPP-Tesradex <https://github.com/TesrabNetwork/CPP-Tesradex>`_ library.

If you use `Go <https://golang.org/>`_ check out the `Go-Tesradex <https://github.com/TesrabNetwork/Go-Tesradex>`_ library.

If you use `PHP <https://secure.php.net/>`_ check out the `PHP-Tesradex <https://github.com/TesrabNetwork/PHP-Tesradex>`_ library.

