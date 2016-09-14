import sys
import logging

from app import config


logging.basicConfig(level=config.LOG_LEVEL)
LOG = logging.getLogger('API')
LOG.propagate = False

COMMON_FORMAT = '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s'
INFO_FORMAT = COMMON_FORMAT
DEBUG_FORMAT = COMMON_FORMAT + ' [in %(pathname)s:%(lineno)d]'
TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S %z'

if config.APP_ENV == 'prod':
    from loggin.handlers import RotationFileHandler
    file_handler = RotationFileHandler('log/app.log', 'a', 1 * 1024 * 1024, 10)
    formatter = logging.Formatter(INFO_FORMAT, TIMESTAMP_FORMAT)
    file_handler.setFormatter(formatter)
    LOG.addHandler(file_handler)

if config.APP_ENV == 'dev' or config.APP_ENV == 'local':
    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(DEBUG_FORMAT, TIMESTAMP_FORMAT)
    stream_handler.setFormatter(formatter)
    LOG.addHandler(stream_handler)


def get_logger():
    return LOG
