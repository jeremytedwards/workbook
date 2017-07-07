# coding=utf-8
import numbers

def move_zeros(array):
    for i,v in reversed(list(enumerate(array))):
        if v is not False and isinstance(v, numbers.Number) and int(float(v)) == 0:
            array.pop(i)
            array.append(0)
    return array



# Other solutions:
#     def move_zeros(arr):
#         l = [i for i in arr if isinstance(i, bool) or i != 0]
#         return l + [0] * (len(arr) - len(l))

    # def move_zeros(array):
    #     return sorted(array, key=lambda x: x == 0 and type(x) is not bool)


# https://www.codewars.com/kata/52597aa56021e91c93000cb0/solutions/python

# Description:
#
# Write an algorithm that takes an array and moves all of the zeros to the end, preserving
# the order of the other elements.
#
# move_zeros([false,1,0,1,2,0,1,3,"a"])
#  returns[false,1,1,2,1,3,"a",0,0]