#!/usr/bin/env python
# pylint: disable=missing-docstring,unused-variable,invalid-name,broad-except

import sys
import json
import os
import logging
import datetime
import boto3
import requests


logger = logging.getLogger('fixerio_example')
BASE_URL = "http://data.fixer.io/api/{dte}?access_key={key}"


def get_fixerio_exchange_rates_day(dte, access_key):
    url = BASE_URL.format(dte=dte.strftime("%Y-%m-%d"), key=access_key)
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()


def upload_json_data_to_s3(s3_bucket, exchange_data):
    client = boto3.client('s3')
    json_str = json.dumps(exchange_data)
    resp = client.put_object(Body=json_str.encode("utf-8"),
                             Bucket=s3_bucket,
                             Key=exchange_data["date"])
    return resp


def main():
    try:
        access_key = os.environ['ACCESS_KEY']
        s3_bucket = os.environ['S3_BUCKET']
    except Exception:
        msg = "Unable to retrieve required environment variables"
        logger.error(msg, exc_info=True)
        sys.exit()

    try:
        exchange_rate_data = get_fixerio_exchange_rates_day(datetime.datetime.utcnow(), access_key)
    except Exception:
        msg = "Unable to retrieve exchange rate data"
        logger.error(msg, exc_info=True)
        sys.exit()

    try:
        upload_resp = upload_json_data_to_s3(s3_bucket, exchange_rate_data)
    except Exception:
        msg = "Unable to upload data to s3."
        logger.error(msg, exc_info=True)
        sys.exit()
