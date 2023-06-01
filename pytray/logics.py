# 12y9mn2b23bm0977yncy7nyr7ycr1


Sqrt = lambda __x: __x**0.5 

def sqrt(x):
    return (x ** 0.5)

def largest_number(*_nums) -> int:
    return max([*_nums])  # type: ignore


def smallest_number(*nums) -> int:
    return min([*nums])


def prime_number(num: int) -> bool:  # type: ignore
    # sourcery skip: remove-unnecessary-cast, simplify-constant-sum, sum-comprehension
    """
    count = sum(num%i == 0 for i in range(1, num+1))
    """
    count=0
    for i in range(1, num+1):
        if num%i==0:
            count+=1
    
    if count>2:
        return False
    if count == 2:
        return True


def sum_of_n_numbers(x: int) -> int:
    return sum(range(x+1))
        
    
def sum_of_squares(number) -> int:
    return ((number * (number + 1) * (2*number + 1)) / 6)  # type: ignore

        
def sum_of_cubes(num) -> int:
    res = (num * (num+1)) * 0.5
    return res * res  # type: ignore



def newtonSqrt(n: float) -> int:  # type: ignore

    approx = 0.5 * n
    better = 0.5 * (approx + n/approx)
    
    while (better != approx):
        approx = better
        better = 0.5 * (approx + n/approx)
        
    return int(approx)

