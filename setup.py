from setuptools import setup
from pathlib import Path


__version__ = 1.0
__author__ = 'PoeticViper'
__credits__ = 'PoeticViper'


cur_dir = Path(__file__).parent
long_description = (cur_dir / 'README.md').read_text()


setup(
    name='vndb_api_wrapper',
    version='1.0.0a',
    description='A wrapper for the VNDB API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/PoeticViper/VNDB-Python-API-Wrapper',
    author='PoeticViper',
    author_email='PoeticViper@users.noreply.github.com',
    license='GPLv3',
    packages=['vndb_api_wrapper', 'vndb_api_wrapper.exceptions', 'vndb_api_wrapper.utils']
)