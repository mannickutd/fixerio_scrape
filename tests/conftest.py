import os
import json
import pytest


TESTS_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def sample_exchange_rate_resp():
    with open(os.path.join(TESTS_DIRECTORY, 'fixtures/sample_exchange_rates.json'), 'r') as fle:
        return json.loads(fle.read())


@pytest.fixture
def sample_access_key():
    return os.environ['ACCESS_KEY']


@pytest.fixture
def sample_s3_bucket():
    return os.environ['S3_BUCKET']
