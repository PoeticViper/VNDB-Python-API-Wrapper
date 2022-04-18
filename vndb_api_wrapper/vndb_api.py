import socket
import ssl
import logging

from .exceptions.vndb_error import VNDBError
from typing import List, Union
from .utils.utils import prepare_request, parse_bytes
from .vndb_info import VNDBInfo


logger = logging.Logger('vndb_api')
EOT = VNDBInfo.END_BYTE


class VNDBAPI:
    """
    Wrapper for the VNDB API
    """
    def __init__(self, username: str, password: str, secure: bool=True):
        self.__socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.__secure = secure
        if self.__secure:
            __context = ssl.create_default_context()
            self.__socket: ssl.SSLSocket = __context.wrap_socket(self.__socket, server_hostname=VNDBInfo.HOST)

        __port = VNDBInfo.SECURE_PORT if secure else VNDBInfo.INSECURE_PORT
        
        self.__socket.connect((VNDBInfo.HOST, __port))
        params = {
            "protocol": 1,
            "client": 'vndb-api-wrapper-python',
            "clientver": 1.0,
            'username': username,
            'password': password
        }
        request = prepare_request('login', params)
        logger.debug("Logging in to VNDB API...")
        res = self.__send_and_recv(request)
        if res == b'ok'+EOT:
            logger.info('Successfully logged in!')
        else:
            logger.error('Failed to authenticate to VNDB API server')
            raise VNDBError(res)

    def __del__(self):
        """
        Close the connection upon object destruction
        """
        logger.info('Closing connection to VNDB API..')
        self.__socket.close()

    def dbstats(self) -> dict:
        """
        Get dbstats for the VNDB
        """
        request = b'dbstats'+EOT
        logger.info('Getting dbstats from VNDB')
        res = self.__send_and_recv_parsed(request)
        return res

    def get(self, search_type: str, flags: Union[str, List[str]], filter: str, options: dict=None) -> dict:
        """
        Query a search to the VNDB. For query syntax, reference https://vndb.org/d11#5
        """
        #  Adds required parenthesis to filter if not present
        if filter[0] != '(' and filter[-1] != ')':
            filter = f'({filter})'
        
        #  If user passed a list of flags to search and not csv's, we parse it here
        if isinstance(flags, list):
            flags = ','.join(flags)

        request = f'get {search_type} {flags} {filter}'
        
        if options:
            request = prepare_request(request, options)
        else:
            request = request.encode('ascii')+EOT

        logger.info(f'Searching VNDB with filter "{filter}"')
        res = self.__send_and_recv_parsed(request)
        return res

    def set(self, search_type: str, db_id: Union[int, str], fields: dict) -> dict:
        """
        Set a user editable value in VNDB
        """
        request = prepare_request(f'set {search_type} {db_id}', fields)
        data = self.__send_and_recv_parsed(request)
        return data

    def __send_and_recv(self, req: bytes) -> bytes:
        """
        Raw function for sending and receiving data through the VNDB API
        Note: There is no error checking in this. For builtin error handling,
        use __send_and_recv_parsed
        """
        self.__socket.send(req)
        logger.info('Sent request to VNDB. Awaiting response')
        chunks = []
        while True:
            chunk = self.__socket.recv(1024)
            chunks.append(chunk)
            if chunk.endswith(b'\x04'):
                break

        logger.info('Successfully received all data for request')

        return b''.join(chunks)

    def __send_and_recv_parsed(self, req: bytes) -> dict:
        req = self.__send_and_recv(req)
        msg, data = parse_bytes(req)
        if msg == 'error':
            raise VNDBError(data)
        
        return data
