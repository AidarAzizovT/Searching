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


def just_search(lst: List[Tuple[str, str]], target: str) -> str:
    for element in lst:
        if element[0] == target:
            return element[1]
    return None


lst = [(str(i), str(i)) for i in range(100)]


start = time()
print(just_search(lst, "43"))
end = time()
print(f"Time of running function 'just_search' is {(end-start)} seconds\n\n\n")


start = time()
lst.sort()
print(binary_search(lst, "43"))
end = time()
print(f"Time of running function 'binary search' is {(end-start)} seconds\n\n\n")
