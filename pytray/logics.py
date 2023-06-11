# 12y9mn2b23bm0977yncy7nyr7ycr1


Sqrt = lambda __x: __x**0.5 

def sqrt(x):
    return (x ** 0.5)

def largest_number(*nums) -> int:
    __num_large: tuple = nums
    return max([*__num_large])  # type: ignore


def smallest_number(*nums) -> int:
    __num_small: tuple = nums
    return min([*__num_small])


def is_prime(num: int) -> bool:  # type: ignore
    # sourcery skip: remove-unnecessary-cast, simplify-constant-sum, sum-comprehension
    """
    count = sum( num % i == 0 for i in range( 1, num + 1 ) )
    """
    __count_var=0
    for i in range(1, num+1):
        if num%i==0:
            __count_var+=1
    
    if __count_var>2:
        return False
    if __count_var == 2:
        return True


def sum_of_n_numbers(x: int) -> int:
    __result_sumofn: int = x
    return sum(range(__result_sumofn + 1))
        
    
def sum_of_squares(number: int) -> int:
    return ((number * (number + 1) * (2*number + 1)) / 6)  # type: ignore

        
def sum_of_cubes(num) -> int:
    res = (num * (num + 1)) * 0.5
    return res * res  # type: ignore



def newtonSqrt(n: float) -> int:  # type: ignore

    __approx = 0.5 * n
    __better = 0.5 * (__approx + n/__approx)
    
    while (__better != __approx):
        __approx = __better
        __better = 0.5 * (__approx + n/__approx)
        
    return int(__approx)

