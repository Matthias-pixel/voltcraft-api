import connexion
import six
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util
from connections import UnknownAliasException, get_address, get_device

def get_info(alias):  # noqa: E501
    try:
        addr = get_address(alias)
        dev = get_device(addr)
        m = dev.request_measurement()
        return { 
            'current': m.current_in_milliampere,
            'frequency': m.frequency_in_hertz,
            'active': m.is_power_active,
            'power': m.power_in_milliwatt,
            'voltage': m.voltage_in_volt
        }
    except UnknownAliasException:
        return {
            "detail": "The requested alias does not exist. If you entered the URL manually please check your spelling and try again.",
            "status": 404,
            "title": "Not Found",
            "type": "about:blank"
        }
    except:
        return {
            "detail": "Could not connect to outlet.",
            "status": 500,
            "title": "Internal Server Error",
            "type": "about:blank"
        }
          