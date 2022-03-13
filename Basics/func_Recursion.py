# Recusrion is a function that calls itself
'''
Factorial of n is
n! = 1*2*3*4.....n
we can also right this as
n!= 1*2*3*4*...(n-3)*(n-2)*(n-1)*n
which can be also written as...
n! = (n-1)!*n
'''
# Using the above formula let's find factorial
'''
# Note- we need to provide a base/break condition in recursion
here, once the n=0 or 1, return n=1 and the recursion should stop!
'''


def fact(n):
    # base condition
    if n == 0 or n == 1:
        return 1
    return fact(n-1)*n


factorial = fact(5)
print(factorial)
