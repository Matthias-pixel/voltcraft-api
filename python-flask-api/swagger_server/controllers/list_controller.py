import connexion
import six
import yaml
from swagger_server.models.outlet import Outlet  # noqa: E501
from swagger_server import util
from connections import outlets

def list_outlets():  # noqa: E501
    aliases = outlets.keys()
    res = []
    for alias in aliases:
        res.append({
            "mac-address": outlets[alias],
            "alias": alias
        })
    return res
