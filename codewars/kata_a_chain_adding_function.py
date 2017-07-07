# coding=utf-8


def add(*args):
    return sum(list(args))

# add_x = lambda x: lambda y: x + y
# add_one = add_x(1)
# add_one(5) # == 6


# from functools import partial
# def add(*args):
#     print(partial(sum, args.iteritems()))
#     return partial(sum, list(args))

#     print([lambda y:x for x in args])
#     return sum([lambda y:x for x in args])

# def add(x):
#     return lambda y: x + y

# def add(*args):
#     print([x for x in args])
#     return sum([x for x in args])

def add(x):
    return lambda y: x + y

add(1)(2)


# https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/train/python
# https://mtomassoli.wordpress.com/2012/03/18/currying-in-python/

# Description
#
# We want to create a function that will add numbers together when called in succession.
#
# add(1)(2);
# // returns 3
# We also want to be able to continue to add numbers to our chain.
#
# add(1)(2)(3); // 6
# add(1)(2)(3)(4); // 10
# add(1)(2)(3)(4)(5); // 15
# and so on.
#
# A single call should return the number passed in.
#
# add(1); // 1
# We should be able to store the returned values and reuse them.
#
# var addTwo = add(2);
# addTwo; // 2
# addTwo + 5; // 7
# addTwo(3); // 5
# addTwo(3)(5); // 10
# We can assume any number being passed in will be valid whole number.