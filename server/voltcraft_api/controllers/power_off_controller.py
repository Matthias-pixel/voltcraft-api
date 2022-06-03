import json, flask
from voltcraft_api import util
from connections import get_address, get_device, reconnect_device, UnknownAliasException

def power_off(alias):  
    try:
        addr = get_address(alias)
        dev = get_device(addr)
        dev.power_off()
        response = flask.make_response("true")
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    except UnknownAliasException:
        res = {
            "detail": "The requested alias does not exist. If you entered the URL manually please check your spelling and try again.",
            "status": 404,
            "title": "Not Found",
            "type": "about:blank"
        }
        response = flask.make_response(json.dumps(res, indent=3))
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    except:
        reconnect_device(alias)
        return False