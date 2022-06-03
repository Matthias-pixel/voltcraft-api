import json
from flask import make_response
from voltcraft_api.models.inline_response200 import InlineResponse200  # noqa: E501
from voltcraft_api import util
from connections import UnknownAliasException, get_address, get_device

def get_info(alias):  # noqa: E501
    try:
        addr = get_address(alias)
        dev = get_device(addr)
        m = dev.request_measurement()
        res = { 
            'current': m.current_in_milliampere,
            'frequency': m.frequency_in_hertz,
            'active': m.is_power_active,
            'power': m.power_in_milliwatt,
            'voltage': m.voltage_in_volt
        }
        response = make_response(json.dumps(res, indent=3))
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
        res = {
            "detail": "Could not connect to outlet.",
            "status": 500,
            "title": "Internal Server Error",
            "type": "about:blank"
        }
        response = make_response(json.dumps(res, indent=3))
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
          