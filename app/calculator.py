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
print ("test 23, pr no. 18. and deleted previous test comments")

#test 25
print ("test 24 is now replaced with test 25 to print)

# test 26
def min_of_list(numbers):
    """
    Returns the minimum number in a list.
    Raises ValueError if the list is empty.
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    return min(numbers)


#test 27
print ("test 27")

#test 28
def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of negative number")
    return x ** 0.5

#test 29
print ("test 29")

#test 30
def subtract_numbers(a, b):
    return a - b

#test 33
print ("removed/swapped tests 31 and 32 to 33!")

#test 35
print ("test 35: removed comment test 34, pr no.: 21")

#test 36
print ("test 36")






