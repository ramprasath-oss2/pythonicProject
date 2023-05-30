#  This is `Math.py` file. 

from __init__ import * 


def Factorial(num: int) -> int:
    const = 1
    for i in range(1, num+1):
        const*=i
    return const


def f(_x: int, /) -> int:
    """
    f(x, /) 
    returns the factorial of x 
    """

    constf = 1

    for iter in range(1, _x+1):
        constf = constf * iter
    return constf


def square(a: float, /) -> float:  # type: ignore # sourcery skip: square-identity
    """
    def square(n, /) -> int: 
        returns the square of the given number. 
    """
    return a*a


def cube(a: float, /):  # sourcery skip: square-identity
    """
    cube(n, /) -> int: 
    returns the cube of the number. 
    """
    return a * a * a


def gcd(d1: int, d2: int) -> int:
    """
    gcd(a, b, /) -> int: 
        Prints the  `Greatest Common Divisor`  of the given two numbers. 
    """
    r = d1 / d2
    while r != 0:
        d1 = d2
        d2 = r  # type: ignore
        r = d1 % d2
    return "%d" % d2  # type: ignore


def fibo(num: int):
    """
    Prints the `Fibonacci Series` up to the specified value of number.
    """ 
    a,b = 0,1
    while a < num:
        print(a, end=' ')
        a,b = b, a+b
    print()
    return 


def permutation(n: int, r: int):
    """
    Prints the `Permutation` value of the specified values.
    """
    if n>r:
        return "%d"%(Factorial(n)/ (Factorial(n-r)))
    return


def combination(n: int, r: int):
    """
    Prints the `Combination` value of the specified values.
    """
    if n>r:
        return "%d"%(Factorial(n) / (Factorial(n-r) * Factorial(r)))
    return


def rectangle(height: int,  base: int) -> float:
    return height * base


def square(length: int) -> int:
    return length**2


def nRoot(num: int, root_num: int) -> float:
    r = 1/root_num
    return num ** r


def absolute(number: int) -> int:
    return number if (number > 0) else -number


def radian(x: int = 1):
    return (180 / PI) * x


def degree(x: int = 1):
    return (PI / 180) * x



#  End of the `main.py` File