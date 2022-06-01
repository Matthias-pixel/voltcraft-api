import yaml
from sem6000 import sem6000
from sem6000.bluetooth_lowenergy_interface.bluepy_interface import BluePyBtLeInterface


if not "devices" in globals():
    devices = {}

if not "outlets" in globals():
    with open("../config.yaml", "r") as config_file:
        config = yaml.full_load(config_file)
        outlets = config["outlets"]

def get_device(addr):
    if (not (addr in devices.keys())) or not devices[addr]._is_connected():
        devices[addr] = sem6000.SEM6000(deviceAddr=addr)
        devices[addr].authorize("0000")
    return devices[addr]