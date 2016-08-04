"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# used in 003b, 003c
from math import sqrt


# 003a || 2016-08-03 || find factors of x by checking all numbers until x,
#                    || generate primes by counting up to largest found factor of x
#                    || with a given number, generate its factors and a list of primes up to its largest factor
#                    || return the largest number in both the primes list and factors list
#                    **** both factor searching and prime generation take IMMENSELY long with large numbers
#                    **** it seems completely unnecessary to have a third function
def factors_via_countup(number):
    lower_factor = [int(x) for x in range(1, number) if number % x == 0]
    return list(set(sorted(lower_factor + [int(number / x) for x in lower_factor])))


def construct_primes(limit):
    return [x for x in range(2, limit + 1) if not [i for i in range(2, x) if not x % i]]


def largest_prime_factor(number, factor_gen, prime_gen):
    factors = factor_gen(number)
    primes = prime_gen(factors[-1])
    return list(set(factors).intersection(primes))[-1]

# largest_prime_factor(600851475143, factors_via_countup, construct_primes)


# 003b || 2016-08-03 || find factors of x by checking all numbers until sqrt(x) then dividing x by the found numbers,
#                    || generate primes by counting up to largest found factor of x
#                    **** prime generation is still extremely long with large numbers
#                    **** it still seems completely unnecessary to have a third function
#
# IMPROVEMENT: for paired factors (x, y) of a number n, n=x*x represents the largest possible value of x.
#              therefore, all y can be derived with far less load by determining all x through divisibility,
#                         then determining all y by y=n/x;
#              therefore, the upper limit for divisibility is sqrt(n), or its next-highest integer value if a range.
def factors_via_sqrt(number):
    lower_factor = [int(x) for x in range(1, int(sqrt(number)) + 1) if number % x == 0]
    return list(set(sorted(lower_factor + [int(number / x) for x in lower_factor])))

# uses same construct_primes(), largest_prime_factor() as in 003a
# largest_prime_factor(600851475143, factors_via_sqrt, construct_primes)


# 003c || 2016-08-03 || find factors of x by checking all numbers until sqrt(x) then dividing x by the found numbers,
#                    || generate a list
#                    **** prime checking still takes extremely long with large numbers
#
# IMPROVEMENT: there is zero purpose in generating ALL primes up to a given limit
#              if a selection of numbers that MAY be prime are already (easily) computed, because
#              every other number not in that selection is an invalid final output anyhow.
#              therefore, only check if valid factors are prime.
def check_if_prime(numbers):
    return sorted([x for x in numbers if x >= 2 if not [i for i in range(2, x) if not x % i]])

# uses same factors_via_sqrt() as in 003b
# check_if_prime(factors_via_sqrt(155))[-1]


# 003d || 2016-08-03 ||
#
# IMPROVEMENT: in the interest of abstraction, rather than modifying check_if_prime() and breaking its usability
#              for any list of numbers, a new function could be defined that is specific to:
#                                       - preferring the largest result (list of numbers in descending order)
#                                       - stopping after the first valid result, since it will also be the largest
#                                       - not evaluating the number itself (and returning it) if it only has two factors
def largest_prime_factor_conditional(factors):
    if len(factors) <= 2:
        return factors[-1]
    else:
        pass
        # incomplete
