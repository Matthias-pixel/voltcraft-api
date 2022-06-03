import connexion
import six
import time
from voltcraft_api import util
from connections import get_address, get_device, UnknownAliasException

def power_on(alias):  # noqa: E501 
    global outlets, devices  
    try:
        addr = get_address(alias)
        dev = get_device(addr)
        dev.power_on()
        return True
    except UnknownAliasException:
        return {
            "detail": "The requested alias does not exist. If you entered the URL manually please check your spelling and try again.",
            "status": 404,
            "title": "Not Found",
            "type": "about:blank"
        }
    except:
        return False