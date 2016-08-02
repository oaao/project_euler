"""
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


# 001a || 2016-08-02 || for-loop all multiples, nested for-loop all integers in range, sum of cumulative set
def for_loop(nums, lower, upper):
    valid_mults = []
    for i in nums:
        for j in range(lower, upper):
            if j % i == 0:
                valid_mults.append(j)
    return sum(set(valid_mults))

# for_loop([3, 5], 0, 1000)


# 001b || 2016-08-02 || list expression with stepped ranges for each multiple, sum of cumulative set
def stepped_ranges(nums, lower, upper):
    valid_mults = []
    for i in nums:
        valid_mults += [j for j in range(lower, upper, i) if j % i == 0]
    return sum(set(valid_mults))

# stepped_ranges([3, 5], 0, 1000)


# 001c || 2016-08-02 || compound list expression, sum of its set (single line!)
def compound_list_expr(nums, lower, upper):
    return sum(set([j for i in nums for j in range(lower, upper, i) if j % i == 0]))

# compound_list_expr([3, 5], 0, 1000)
