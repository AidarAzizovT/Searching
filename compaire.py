import string
from random import randint
from time import time
from typing import List,Union, Tuple

alphabet = string.ascii_lowercase


def make_rand_names(count):
    names = []
    while len(names) < count:
        name = "".join([alphabet[randint(0, len(alphabet) - 1)] for j in range(randint(3, 11))])
        if name not in names:
            names.append(name)
    return names

def binary_search(lst, target):
    lo = 0
    hi = len(lst)
    while lo < hi:
        mid = (lo + hi)//2
        mid_val = lst[mid][0]
        if mid_val < target:
            lo = mid + 1
        elif mid_val > target:
            hi = mid 
        else:
            return lst[mid][1]


def simple_search(lst: List[Tuple[str, str]], target: str) -> str:
    for element in lst:
        if element[0] == target:
            return element[1]
    return None


result_dict = {'N': [i for i in range(1, 10)], 'Кол-во контактов': [10**i for i in range(1, 10)], 'Simple search': [], 'Binary Search': []}
for j in range(1, 5):
    N = 10**j
    lst = [(str(i), str(i)) for i in range(N)]


    start = time()
    result_list = [simple_search(lst, str(randint(0, N - 1))) for i in range(100)]
    end = time()
    result_dict['Simple search'].append((end - start)/100)

    start = time()
    result_list = [binary_search(lst, str(randint(0, N - 1))) for i in range(100)]
    end = time()
    result_dict['Binary Search'].append((end - start)/100)

print(result_dict)