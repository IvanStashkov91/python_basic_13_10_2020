"""This is my module
"""

def my_enumerate(iter_object, start = 0):
    """ Some doc string
    :param iter_object:
    :param start:
    :return:
    """
    for itm in iter_object:
        yield start, itm
        start += 1

def my_cycle(iter_object):
    idx = 0
    while True:
        try:
            yield iter_object[idx]
            idx += 1
        except IndexError:
            idx = 0
