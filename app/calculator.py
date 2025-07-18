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
#test08
print ("test 8")
#test 09
print ("test 9")
#test 10
print ("test 10")
#test 11
def average(*args):
    if not args:
        raise ValueError("At least one number is required")
    return sum(args) / len(args)
#test 12
print ("test 12")
#test 13
print ("test 13")
#test 14
print ("test 14")

#test 15
print ("test 15")

# test 16
def max_of_list(numbers):
    """
    Returns the maximum number in a list.
    Raises ValueError if the list is empty.
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)

#test 17
print ("test 17")
#test 18
print ("test 18")
#test 19
print ("test 19")
#test 20
print ("test 20")
#test 21
print ("test 21")
#test 22
print ("test 22, pr no. 17")








