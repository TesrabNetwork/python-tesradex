#!/usr/bin/env python
# coding=utf-8

from tesradex.client import Client
from tesradex.exceptions import TesradexResolutionException
import pytest

client = Client('api_key', 'api_secret')


def test_resolution_exception():
    """Test Resolution Exception"""

    with pytest.raises(TesradexResolutionException):

        client.get_kline_data('TDEX-BTC', 'invalid-res', 1510156800, 1510278278)
