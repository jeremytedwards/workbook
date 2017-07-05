# coding=utf-8

def find_deleted_number(arr, mixed_arr):
    return 0 if len(arr) < 1 else sum(arr) - sum(mixed_arr)


#  Other Solutions:
#     def find_deleted_number(arr, mixed_arr):
#         return sum(arr) - sum(mixed_arr)



# https://www.codewars.com/kata/lost-number-in-number-sequence/train/python

# Description:
#
# An ordered sequence of numbers from 1 to N is given. One number might have deleted from it, then the remaining numbers were mixed. Find the number that was deleted.
#
# Example:
#
# The starting array sequence is [1,2,3,4,5,6,7,8,9]
# The mixed array with one deleted number is [3,2,4,6,7,8,1,9]
# Your function should return the int 5.
# If no number was deleted from the array and no difference with it, your function should return the int 0.
#
# Note that N may be 1 or less (in the latter case, the first array will be []).