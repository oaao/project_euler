"""
https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


# 002__PREPa || 2016-08-02 || defining a Fibonacci sequence via term replacement
def term_replacement(limit):
    fib_term1 = 0
    fib_term2 = 1
    list_terms = []
    while fib_term1 + fib_term2 < limit:
        next = fib_term1 + fib_term2
        fib_term1 = fib_term2
        fib_term2 = next
        list_terms.append(fib_term2)
    return list_terms


# 002_PREPb || 2016-08-02 || defining a Fibonacci sequence via recursively iterating over a list
def list_recursion(limit):
    fib_seq = [0, 1]
    while (fib_seq[-2] + fib_seq[-1]) < limit:
        fib_seq.append(fib_seq[-2] + fib_seq[-1])
    return fib_seq


# 002_PREPc || 2016-08-02 || defining a Fibonacci sequence via multiple reassignment and (default) keyword arguments
#                         || ** BORROWED: beginning terms are keyword arguments
#                         || ** BORROWED: x, y = y, (x + y) formulation to avoid assigning a third term
def two_recursive_kwargs(limit, a=0, b=1):
    # keyword arguments define natural Fibonacci sequence by default, but can be overridden in function call
    fib_seq = [a, b]
    while a + b < limit:
        a, b = b, (a + b)
        fib_seq.append(b)
    return fib_seq
