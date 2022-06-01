import connexion
import six
import yaml

from swagger_server.models.outlet import Outlet  # noqa: E501
from swagger_server import util


def list_outlets():  # noqa: E501
    with open("../config.yaml", "r") as config_file:
        config = yaml.full_load(config_file)
        print(config)
        aliases = config["outlets"].keys()
        res = []
        for alias in aliases:
            res.append({
                "mac-address": config["outlets"][alias],
                "alias": alias
            })
        return res
