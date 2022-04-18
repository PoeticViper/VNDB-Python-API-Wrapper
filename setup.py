from setuptools import setup


__version__ = 1.0
__author__ = 'PoeticViper'
__credits__ = 'PoeticViper'


setup(
    name='vndb_api_wrapper',
    version='1.0.0',
    description='A wrapper for the VNDB API',
    url='https://github.com/PoeticViper/VNDB-Python-API-Wrapper',
    author='PoeticViper',
    author_email='PoeticViper@users.noreply.github.com',
    license='GPLv3',
    packages=['vndb_api_wrapper', 'vndb_api_wrapper.exceptions', 'vndb_api_wrapper.utils']
)