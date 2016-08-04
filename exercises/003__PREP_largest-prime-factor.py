"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# All logic below begins with a sequence of primes up to x, and then proceeds to examine factors of x.
# This is not feasible for very large numbers.
# As such, that logic needs to be reversed: First, determine factors of x, then, determine which are prime.


# 003_PREPa || 2016-08-03 || DEFUNCT: all factors of x should be found first, otherwise the looping is too inefficient
#                         || 2 added manually
#                         || primes generated as differences of squares, then filtered
def diff_sq(limit):
    nums = [2]
    for i in range(2, limit):
        nums.append((i ** 2) - ((i - 1) ** 2))
    return nums


def filter_squares(constructor):
    to_filter = []
    for i in constructor:
        for j in constructor:
            if i % j == 0 and i != j:
                to_filter.append(i)
    return sorted(set(constructor) - set(to_filter))


def largest_factor(possible_factors, number):
    return [x for x in possible_factors if number % x == 0][-1]

# example_number = 100
# largest_factor(filter_squares(diff_sq(example_number))))


# 003_PREPb || 2016-08-03 || DEFUNCT: all factors of x should be found first, otherwise the looping is too inefficient
#                    || nested list expression
def nested_list_expr_primes(limit):
    return [x for x in range(2, limit) if not [i for i in range(2, x) if not x % i]]

# example_number = 100
# largest_factor(nested_list_expr_primes(example_number), example_number)
