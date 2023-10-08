# File containing all the pre-defined values

import configparser
config = configparser.ConfigParser()
config.read('secrets.ini')

DEBUG = True
HEADLESS = False
URL = "https://branddb.wipo.int/en/quicksearch"
# URL = "https://ipinfo.io/"
INPUT = "Red Barn"
DEFAULT_DELAY = 15
RESULT_REGEX = r'Displaying \d+-\d+ of (\d+) results'

# Proxy settings
USE_PROXY = config.getboolean('PROXY', 'USE_PROXY')
PROXY_HOST = config.get('PROXY', 'PROXY_HOST').strip()
PROXY_PORT = config.getint('PROXY', 'PROXY_PORT')
PROXY_USER = config.get('PROXY', 'PROXY_USER').strip()
PROXY_PASS = config.get('PROXY', 'PROXY_PASS').strip()
