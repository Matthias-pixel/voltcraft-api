import connexion
import six
import time
from swagger_server import util
from connections import outlets, get_device

def power_off(alias):  
    try:
        addr = outlets[alias]
        dev = get_device(addr)
        dev.power_off()
        return True
    except:
        return False