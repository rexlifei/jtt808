"""
This class expect two argument,one is a request (a dicts type)
the another is a template split by a "|" string
"""
import sys

sys.path.append("..")
from utils.check_code import check


def render(request, template):
    """

    :param template:
    :type request: object
    """
    temp = []
    each = template.split("|")
    for item in each:
        if item in request:
            if request[item]:
                for k in request[item]:
                    temp.append(k)
    temp.append(request['crc'])     #Auto loader the crc for value
    check_code = check(temp)
    temp[-1] = check_code
    temp.insert(0, 126)
    temp.append(126)
    return tuple(temp)

def render_to_tuple(request):
    pass