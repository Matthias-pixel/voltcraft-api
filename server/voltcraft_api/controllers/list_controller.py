import connexion
from flask import make_response
import json
from voltcraft_api.models.outlet import Outlet  # noqa: E501
from voltcraft_api import util
from connections import outlets

def list_outlets():  # noqa: E501
    aliases = outlets.keys()
    res = []
    for alias in aliases:
        res.append({
            "mac-address": outlets[alias],
            "alias": alias
        })
    response = make_response(json.dumps(res, indent=3))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
