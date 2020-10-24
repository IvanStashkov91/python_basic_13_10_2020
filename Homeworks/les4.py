#import time
from time import (
    sleep,
    time,
    timezone,
)
import math
import my_module
import datetime as dt
from time import sleep as sl

from itertools import cycle
from collections import defaultdict


#some_list = ['a', 'b', 'c', 'd']

#ф-я enumerate
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

#for value in my_module.my_cycle(some_list):
#    print(value)
#    sleep(2)

def anagram_search(itr_obj: list):
    pre_result = defaultdict(list)
    for itm in itr_obj:  #обход списка
        pre_result[''.join(sorted(itm))].append(itm)
        #try:
            #pre_result[''.join(sorted(itm))].append(itm)
        #except KeyError:
            #pre_result[''.join(sorted(itm))] = [itm]
    return list(pre_result.values())



#test = ['hello', 'dear', 'gb', 'olelh', 'arde']
#result = [['hello', 'olelh'], ['dear', 'arde'], ['gb',]]
#res = anagram_search(test)
#print(res)

def some(start_num):
    def wrap(*args, **kwargs):
        return start_num + sum(args)

    return wrap

def log(func):
    def wrap(*args, **kwargs):
        print(f'{time()} -- {func.__name__}, {args}, {kwargs}')
        result = func(*args, *kwargs)
        print(f'{time()} END WORK')
        return result
    return wrap

@log
def some_a(a, b):
    return a + b

@log
def some_b(a, b, c):
    return (a + b) ** c

#a = some(12)

print(some_a(1, 2))
print(some_b(1, 2, 3))
#a = [3, 4, 11, 13, 12, 11, 4, 4, 7, 3, 8, 12, 11, 22, 18, 15, 13, 12]
#a_result = [4, 12, 4, 4, 8, 12, 22, 18, 12]

#result = [itm for itm in a if not itm & 1]  #list comprehencion
#for itm in a:
#    if not itm & 1: #четные числа
#        result.append(itm)


#result2 = {idx: itm for idx, itm in enumerate(a) if not itm & 1} # для словаря
#print(result)
#print(result2)

