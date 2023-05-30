# This is `main.py` file. 


"""
  /* Copyright ©
  /* 

  
"""

from __init__ import * 
import math 
from time import sleep
from ast import FunctionDef


def digit_sum(n: int):
    """
    digit_sum(n, /) -> int
    reutrns the sum value of the given digit
    """
    i, j = 0, 0
    sn = str(n) # type: ignore
    while i < len(sn):
        j += int(sn[i])
        i += 1
    return j


def add_tuple(Tuple: tuple):
    """
    add_tuple(Tuple, ...) -> tuple
    reutrns the sum of the integer elements present in the given tuple 
    """
    s, i = 0, 0
    while i < len(Tuple):
        s += Tuple[i]
        i += 1
    return s 


def Factorial(n: int):
    return 1 if n in {0, 1} else n * Factorial(n - 1)


def radian(x=1):
    return (180 / math.pi) * x


def degree(x=1):
    return (math.pi / 180) * x


def work_done(force=1, direction=1):
    return force * direction


def mid_value_list(x=[]):
    # sourcery skip: default-mutable-arg, extract-duplicate-method, inline-variable, remove-redundant-if, simplify-division
    l = len(x)
    if (l%2) == 0:
        n = (l/2)
        i = int(n)
        return x[i]
    if l%2 != 0:
        m = (l/2)
        j = int(m)
        return x[j]


def mid_value_tuple(x: tuple):
    # sourcery skip: extract-duplicate-method, inline-variable, remove-redundant-if, simplify-division
    l = len(x)
    if (l%2) == 0:
        n = (l/2)
        i = int(n)
        return x[i]
    if l%2 != 0:
        m = (l/2)
        j = int(m)
        return x[j]


def n_comma_n(num=2, choice="even" or "odd"):
    
    if choice in {"Odd", "ODD", "odd", "O", "o"}:    
        for i in range(1, 2*(num + 1), 2):
            print(i, i, end='\t')
    
    elif choice in {"Even", "EVEN", "even", "E", "e"}:
        for i in range(0, 2*(num + 1), 2):
            print(i, i, end='\t')
    
    else:
        return num


def Freons(fluorine: int = 1, carbon: int = 1, hydrogen: int = 0):
    """
    def Freons( fluorine, carbon, hydrogen, bool = False ) -> str: 
        returns the `Freons`  value. 
    """
    h, f, c = hydrogen, fluorine, carbon
    return f"Freon-{ c-1 }{ h+1 }{ f }"


def str_with_space(string: str):
    i=0
    return f"{string[0]} {string[i + 1:]}"


def add_all_values(*num: float or int) -> float:
    # This function is created in the date {07.07.2021}
    s, i = 0, 0
    while i < len(num):
        s += num[i]
        i += 1
    return s


def Product_all_values_Fn(*num: float):
    # This function is created in the date {07.07.2021}
    s, i = 1, 0
    while i < len(num):
        s *= num[i]
        i += 1
    return s


add_all_numbers = lambda *num: sum(num) # date -> {28.10.2021}


def product(*num: float):
    s = 1
    for i in num:
        s *= i
    return s


Square = lambda x, y: x*y 

multiply = lambda *args: product(*args) #  date -> {03/04/2023}

multiply_all_numbers = lambda *val: product(*val)

reverseList = lambda *var: list(var)[::-1]

reverseTuple = lambda *var: tuple(var)[::-1]

reverseString = lambda vals: str(vals)[::-1]

reverseNumber = lambda val: int(str(val)[::-1])

reverseDigit = lambda val: int(str(val)[::-1])

removeDuplicateElements = lambda *var: sorted(list(set(var)))


def list_elements_to_string(var: list):
    """
    Converts the List to a single string
    """
    j = 0
    s = ""
    for i in var:
        j += var[i]
        s += str(j)
    return s


def create_dict(limit: int, function : FunctionDef ) -> object: 
    """
    Creates the  `Function`  in the  `Dictionary` with the specified `Range`. 
    """
    return {x : function for x in range(limit)}  # type: ignore


#  25-02-2023

def cPrintf(text: str = ..., iter_range: int = 1, delay: int = 0) -> None:
    for _ in range(iter_range):
        sleep(delay)
        print(text)
    return