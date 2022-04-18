# VNDB-Python-API-Wrapper
API Wrapper for the VNDB API Server
Requires Python3.6+

Basic code example
```
from vndb_api_wrapper.vndb_api import VNDBAPI
...
vndb_api = VNDBAPI(<your username>, <your password>)

#  Example of searching for a VN anime of the visual novel with id = 17 using "get"
data = vndb_api.get('vn', 'basic,anime', '(id = 17)')
```

# Installation Instructions
```
git clone https://github.com/PoeticViper/VNDB-Python-API-Wrapper.git
cd VNDB-Python-API-Wrapper
pip3 install . 
```
