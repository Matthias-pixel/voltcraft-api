import yaml, sys
from sem6000.sem6000 import sem6000
from time import sleep

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
    max_retries = 5
    for alias in outlets.keys():
        addr = outlets[alias]
        for retry in range(1, max_retries+1):
            try:
                devices[addr] = sem6000.SEM6000(deviceAddr=addr, timeout=3)
                devices[addr].authorize("0000")
                break
            except:
                print(f"Could not connect to outlet {alias} with mac address {addr}. Retry ({retry}/{max_retries})")
                sleep(5)
                if retry == max_retries:
                    sys.stderr.write(f"Could not connect to outlet {alias} with mac address {addr} after {max_retries} attempts. Aborting.\n")
                    sys.exit(1)
                continue

def reconnect_device(alias):
    max_retries = 5
    addr = outlets[alias]
    for retry in range(1, max_retries+1):
        try:
            devices[addr].disconnect()
            sleep(5)
            devices[addr] = sem6000.SEM6000(deviceAddr=addr, timeout=3)
            devices[addr].authorize("0000")
            break
        except:
            print(f"Could not connect to outlet {alias} with mac address {addr}. Retry ({retry}/{max_retries})")
            if retry == max_retries:
                sys.stderr.write(f"Could not connect to outlet {alias} with mac address {addr} after {max_retries} attempts. Aborting.\n")
                sys.exit(1)
            continue

pre_connect()