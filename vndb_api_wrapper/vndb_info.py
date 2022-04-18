class VNDBInfo:
    HOST: str = 'api.vndb.org'
    SECURE_PORT: int = 19535
    INSECURE_PORT: int = 19534
    #  End of transmission byte for VNDB api server
    END_BYTE: bytes = b'\x04'

    def __init__(self):
        raise ReferenceError('Do not instanciate this class')