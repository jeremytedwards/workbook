# coding=utf-8

# [ Easy ]
# https://leetcode.com/problems/two-sum/#/description
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

list.insert()

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i1, v1 in enumerate(nums):
            for i2, v2 in enumerate(nums[i1 + 1:]):
                if v1 + v2 == target:
                    result = [i1, i2 + i1 + 1]
                    break

        return result


if __name__ == "__main__":
    test = Solution()

    results = test.twoSum([2, 7, 11, 15], 9) # [0, 1]
    print(results)

    results = test.twoSum([2, 7, 11, 15], 18) # [1, 2]
    print(results)

    results = test.twoSum([2, 7, 11, 15], 17) # [1, 3]
    print(results)