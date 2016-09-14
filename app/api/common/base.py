import falcon
import json

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict

from app import log
from app.config import BRAND_NAME, POSTGRES
from app.database import engine
from app.errors import NotSupportedError

LOG = log.get_logger()


class BaseResource(object):
    HELLO_WORLD = {
        'server': '{0}'.format(BRAND_NAME),
        'database': '{0} ({1})'.format(engine.name, POSTGRES['host']),
    }

    def to_json(self, body_dict):
        return json.dumps(body_dict)

    def on_get(self, req, res):
        if req.path == '/':
            res.status = falcon.HTTP_200
            res.body = self.to_json(self.HELLO_WORLD)
        else:
            raise NotSupportedError(method='GET', url=req.path)

    def on_post(self, req, res):
        raise NotSupportedError(method='POST', url=req.path)

    def on_put(self, req, res):
        raise NotSupportedError(method='PUT', url=req.path)

    def on_delete(self, req, res):
        raise NotSupportedError(method='DELETE', url=req.path)
