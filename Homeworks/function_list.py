"""
In this case I use the functions for writing my code in after lesson homework.
"""

# my_sum ################################################################################################
def my_sum(list):
    ''' Sum function implementation
    :param list:
    :return: sum of numbers in list
    '''
    result = 0
    for itm in list:
        result = result + float(itm)
    return result

# my_range ################################################################################################
def my_range(start, stop, step=1):
    ''' Range function implementation
    :param start:
    :param stop:
    :param step:
    :return: a sequence of number from start to stop (not include) with step.
    '''
    try:
        while start < stop:
            yield start
            start += step
    except ValueError:
        print('use only number')

# my_enumerate ###############################################################################################
def my_enumerate(iter_object, start = 0):
    """ Enumerate function implementation
    :param iter_object:
    :param start:
    :return: numbered list
    """
    for itm in iter_object:
        yield start, itm
        start += 1


# my_cycle ################################################################################################
def my_cycle(iter_object):
    ''' Cycle function implementation
    :param iter_object:
    :return:
    '''
    idx = 0
    while True:
        try:
            yield iter_object[idx]
            idx += 1
        except IndexError:
            idx = 0

# my_fact ################################################################################################
def my_fact(number):
    ''' Factorial function implementation
    :param number:
    :return: factorial of number
    '''
    num = 1
    for el in my_range(1, number + 1):
        num = num * el
        yield num

# my_reduse ################################################################################################
_initial_missing = object()
def my_reduce(function, sequence, initial=_initial_missing):
    """
    reduce(function, sequence[, initial]) -> value
    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
    """

    it = iter(sequence)

    if initial is _initial_missing:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError("reduce() of empty sequence with no initial value") from None
    else:
        value = initial

    for element in it:
        value = function(value, element)

    return value

try:
    from _functools import my_reduce
except ImportError:
    pass
