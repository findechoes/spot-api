import os
import configparser
#from itertools import chain


BRAND_NAME = 'Find Echoes'

SECRET_KEY = ''
UUID_LEN = 10
UUID_ALPHABET = ''.join(map(chr, range(48, 58)))
TOKEN_EXPIRES = 3600

APP_ENV = os.environ.get('APP_ENV') or 'local'  # or 'prod' to load prod
print("APP_ENV: {}".format(APP_ENV))
INI_FILE = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../conf/{}.ini'.format(APP_ENV)
)

CONFIG = configparser.ConfigParser()
CONFIG.read(INI_FILE)
POSTGRES = CONFIG['postgres']
if APP_ENV == 'dev' or APP_ENV == 'prod':
    DB_CONFIG = (POSTGRES['user'], POSTGRES['password'], POSTGRES['host'], POSTGRES['database'])
    DATABASE_URL = "postgresql+psycopg2://{0}:{1}@{2}/{3}".format(*DB_CONFIG)
else:
    DB_CONFIG = (POSTGRES['host'], POSTGRES['database'])
    DATABASE_URL = "postgresql+psycopg2://{0}/{1}".format(*DB_CONFIG)
    print(DATABASE_URL)

DB_ECHO = True if CONFIG['database']['echo'] == 'yes' else False
DB_AUTOCOMMIT = True

print(CONFIG['logging'])
LOG_LEVEL = CONFIG['logging']['level']
