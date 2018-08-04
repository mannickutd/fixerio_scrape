#!/usr/bin/env python
import datetime
import json
from unittest.mock import (patch, Mock)
import requests_mock
from fixerio_scrape.main import (get_fixerio_exchange_rates_day,
                                 BASE_URL,
                                 upload_json_data_to_s3)


def test_get_fixerio_exchange_rates_day(sample_exchange_rate_resp, sample_access_key):
    with requests_mock.mock() as m:
        dte = datetime.datetime.utcnow()
        url = BASE_URL.format(dte=dte.strftime("%Y-%m-%d"), key=sample_access_key)
        m.get(url, text=json.dumps(sample_exchange_rate_resp))
        resp = get_fixerio_exchange_rates_day(dte, sample_access_key)
        assert 'date' in resp
        assert 'rates' in resp


def test_upload_json_data_to_s3(sample_exchange_rate_resp, sample_s3_bucket):
    with patch('fixerio_scrape.main.boto3.client') as mock_method:
        upload_json_data_to_s3(sample_s3_bucket, sample_exchange_rate_resp)
