# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from utils import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )


class TestHasPosition:
    def test_example1(self):
        root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
        targetSum = 22
        tree = TreeNode.from_list(root)
        expected = True
        result = Solution().hasPathSum(tree, targetSum)
        assert result == expected

    def test_example2(self):
        root = [1, 2, 3]
        targetSum = 5
        tree = TreeNode.from_list(root)
        expected = False
        result = Solution().hasPathSum(tree, targetSum)
        assert result == expected

    def test_example3(self):
        root = []
        targetSum = 0
        tree = TreeNode.from_list(root)
        expected = False
        result = Solution().hasPathSum(tree, targetSum)
        assert result == expected
