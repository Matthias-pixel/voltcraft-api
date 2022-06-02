import yaml
from sem6000 import sem6000
from sem6000.bluetooth_lowenergy_interface.bluepy_interface import BluePyBtLeInterface


if not "devices" in globals():
    devices = {}

if not "outlets" in globals():
    with open("../config.yaml", "r") as config_file:
        config = yaml.full_load(config_file)
        outlets = config["outlets"]

class UnknownAliasException(Exception):
    def __init__(self):
        return

def get_address(alias):
    if not alias in outlets.keys():
        raise UnknownAliasException()
    return outlets[alias]

def get_device(addr):
    if (not (addr in devices.keys())) or not devices[addr]._is_connected():
        devices[addr] = sem6000.SEM6000(deviceAddr=addr, timeout=3)
        devices[addr].authorize("0000")
    return devices[addr]

def pre_connect():
    for addr in outlets.values():
        devices[addr] = sem6000.SEM6000(deviceAddr=addr, timeout=3)
        devices[addr].authorize("0000")

pre_connect()