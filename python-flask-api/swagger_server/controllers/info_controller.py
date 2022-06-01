import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def get_info(alias):  # noqa: E501
    """Returns measurement data from an outlet.

    d # noqa: E501

    :param alias: outlet alias
    :type alias: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'
