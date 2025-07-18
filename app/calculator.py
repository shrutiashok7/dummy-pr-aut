def add(a, b): return a + b
def subtract(a, b): return a - b
#test 01
def subtract(a, b):
    return a - b
#test 02
def square(x):
    return x * x
#test 03
def cube(a):
    return a * a * a
#test 04
def power(x, y):
    return x ** y
#test 05
def modulo(a, b):
    return a % b
#test 06
import math

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)
#test 07
def percentage(part, whole):
    return (part / whole) * 100

#test 11
def average(*args):
    if not args:
        raise ValueError("At least one number is required")
    return sum(args) / len(args)


# test 16
def max_of_list(numbers):
    """
    Returns the maximum number in a list.
    Raises ValueError if the list is empty.
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)


#test 23
print ("test 22, pr no. 18. and deleted previous test comments")








