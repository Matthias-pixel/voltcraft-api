import connexion
import six
import time, yaml

from swagger_server import util


def power_on(alias):  # noqa: E501
    time.sleep(2)
    return (alias == "hallo")
