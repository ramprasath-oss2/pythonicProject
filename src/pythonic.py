#  File Created: 12/04/2023

#------------------------------------------------

"""
    This File contains some Shortcuts 
    and logics in Python.
"""



#    Lambda Expressions or single line Code.

Sqrt = lambda x: x**0.5

Square = lambda x, y: x*y 

multiply = lambda *args: product(*args) #  date -> {03/04/2023}

multiply_all_numbers = lambda *val: product(*val)

reverseList = lambda *var: list(var)[::-1]

reverseTuple = lambda *var: tuple(var)[::-1]

reverseString = lambda vals: str(vals)[::-1]

reverseNumber = lambda val: int(str(val)[::-1])

reverseDigit = lambda val: int(str(val)[::-1])

removeDuplicateElements = lambda *var: sorted(list(set(var)))


#  Utility Methods

def product(*num: float):
    s = 1
    for i in num:
        s *= i
    return s

#  Utility Classes
