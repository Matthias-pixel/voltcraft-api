import connexion
import six
from sem6000 import sem6000
from sem6000.bluetooth_lowenergy_interface.bluepy_interface import BluePyBtLeInterface
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util
from connections import outlets, get_device

def get_info(alias):  # noqa: E501
    try:
        addr = outlets[alias]
        dev = get_device(addr)
        m = dev.request_measurement()
        return { 
            'current': m.current_in_milliampere,
            'frequency': m.frequency_in_hertz,
            'active': m.is_power_active,
            'power': m.power_in_milliwatt,
            'voltage': m.voltage_in_volt
        }
    except:
        return { 
            'current': -1,
            'frequency': -1,
            'active': -1,
            'power': -1,
            'voltage': -1
        }
          