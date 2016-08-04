# coding=utf-8

# Found solution
#################################
def validate(n):
    digits = [int(x) for x in str(n)]
    for x in xrange(len(digits)-2, -1, -2):
        digits[x] = sum(map(int, str(digits[x] * 2)))
    return sum(digits) % 10 == 0


# Your Solution
###################################

def validate(n):
    print n
    list_n = [int(i) for i in str(n)]
    nines = 0
    if len(list_n) % 2 == 0:
        even_sum = 0
        for i in list_n[::2]:
            if 2 * i > 9:
                nines += 1
            even_sum += 2 * i
        even_sum = even_sum - 9 * nines
        n_sum = sum(list_n[1::2]) + even_sum
    else:
        odd_sum = 0
        for i in list_n[1::2]:
            if 2 * i > 9:
                nines += 1
            odd_sum += 2 * i
        odd_sum = odd_sum - 9 * nines
        n_sum = sum(list_n[::2]) + odd_sum
    print n_sum
    return n_sum % 10 == 0


# TODO: Replace examples and use TDD development by writing your own tests
# These are some of the methods available:
#   test.expect(boolean, [optional] message)
#   test.assert_equals(actual, expected, [optional] message)
#   test.assert_not_equals(actual, expected, [optional] message)

# You can use Test.describe and Test.it to write BDD style test groupings

test.assert_equals(validate(123), False)
test.assert_equals(validate(1), False)