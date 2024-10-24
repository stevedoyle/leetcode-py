# Title: 104. Maximum Depth of Binary Tree
# URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy

from typing import Optional
from utils import TreeNode, create_tree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return 0


class TestMaxDepth:
    def test_example1(self):
        root = create_tree([3, 9, 20, None, None, 15, 7])
        assert Solution().maxDepth(root) == 3

    def test_example2(self):
        root = create_tree([1, None, 2])
        assert Solution().maxDepth(root) == 2
