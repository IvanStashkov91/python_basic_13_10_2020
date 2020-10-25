"""
In this case I use the functions for writing my code in after lesson homework.
"""

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
