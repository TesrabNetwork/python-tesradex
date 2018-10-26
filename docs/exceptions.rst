Exceptions
==========

TesradexResponseException
-----------------------

Raised if a non JSON response is returned

TesradexAPIException
------------------

On an API call error a tesradex.exceptions.TesradexAPIException will be raised.

The exception provides access to the

- `status_code` - response status code
- `response` - response object
- `message` - Tesradex error message=
- `request` - request object if available

.. code:: python

    try:
        client.get_coin_list()
    except TesradexAPIException as e:
        print(e.status_code)
        print(e.message)

TesradexResolutionException
-------------------------

Raised if resolution entered for kline data is invalid
