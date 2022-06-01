import connexion
import six
import time, yaml
from sem6000 import sem6000
from sem6000.bluetooth_lowenergy_interface.bluepy_interface import BluePyBtLeInterface
from swagger_server import util


def power_off(alias):   
    outlets={}
    with open("../config.yaml", "r") as config_file:
        config = yaml.full_load(config_file)
        outlets = config["outlets"]
    try:
        dev = sem6000.SEM6000(deviceAddr=outlets[alias])
        dev.authorize("0000")
        dev.power_off()
        return True
    except:
        return False