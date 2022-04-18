from ast import parse
from typing import Union
from ..utils.utils import parse_bytes


class VNDBError(Exception):
    def __init__(self, resp: Union[bytes, dict]):
        if isinstance(resp, bytes):
            _, data = parse_bytes(resp)
        else:
            #  resp must be a <dict> object
            data = resp
        self.message = f'An "{data["id"]}" error occured when trying to use the VNDB api: "{data["msg"]}"'
        super().__init__(self.message)