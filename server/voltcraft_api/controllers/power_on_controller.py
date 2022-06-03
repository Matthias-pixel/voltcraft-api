import json
from flask import make_response
from voltcraft_api import util
from connections import get_address, get_device, UnknownAliasException

def power_on(alias):  # noqa: E501 
    global outlets, devices  
    try:
        addr = get_address(alias)
        dev = get_device(addr)
        dev.power_on()
        response = make_response("true")
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    except UnknownAliasException:
        res = {
            "detail": "The requested alias does not exist. If you entered the URL manually please check your spelling and try again.",
            "status": 404,
            "title": "Not Found",
            "type": "about:blank"
        }
        response = make_response(json.dumps(res, indent=3))
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    except:
        response = make_response("false")
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response