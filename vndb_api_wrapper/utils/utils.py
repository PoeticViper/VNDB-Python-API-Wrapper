import json

from typing import Tuple
from ..vndb_info import VNDBInfo


def parse_bytes(b: bytes) -> Tuple[str, dict]:
    """
    Parse the response returning the message code and a json object
    with the results
    """
    msg, data_str = b[:-1].decode('utf-8').split(' ', 1)
    data = json.loads(data_str)
    return msg, data


def prepare_request(command: str, params: dict) -> bytes:
    """
    Parse the request into a readable format for the API server
    """
    query = command + ' ' + json.dumps(params)

    return query.encode('ascii')+VNDBInfo.END_BYTE