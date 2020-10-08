import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname("__file__")))
from app import create
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


@pytest.fixture(scope="package")
def event():
    event = {'body': '{"text": "Learn Serverless"}'}
    return event


def test_handler(event, context, ddb_tbl):
    old_cnt = ddb_tbl.scan(Select='COUNT')['Count']
    create.handler(event, context)
    logger.info("create test success")
    assert ddb_tbl.scan(Select='COUNT')['Count'] - old_cnt == 1
