import connexion
import six
import time
from swagger_server import util
from connections import outlets, get_device

def power_on(alias):  # noqa: E501 
    global outlets, devices  
    try:
        addr = outlets[alias]
        dev = get_device(addr)
        dev.power_on()
        return True
    except:
        return False