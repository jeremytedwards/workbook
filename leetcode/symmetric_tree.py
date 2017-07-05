# coding=utf-8

# [ Medium ]
# https://leetcode.com/problems/symmetric-tree/#/description
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self._compareIter(root[1:2]) and self._compareIter(root[3:6])

    def _compareIter(self, subtree):
        return subtree == subtree[::-1]

    # def _compareRecusive(self, root):




if __name__ == "__main__":
    this = Solution()
    print(this.isSymmetric([1, 2, 2, 3, 4, 4, 3]))
    print(this.isSymmetric([1, 2, 2, None, 3, None, 3]))
