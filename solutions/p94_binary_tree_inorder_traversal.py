# Title: 94. Binary Tree Inorder Traversal
# URL: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Difficulty: Medium

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root, res):
        if root is None:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)


class TestInorderTraversal:
    def test_example1(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        assert Solution().inorderTraversal(root) == [1, 3, 2]

    def test_example2(self):
        root = None

        assert Solution().inorderTraversal(root) == []

    def test_example3(self):
        root = TreeNode(1)

        assert Solution().inorderTraversal(root) == [1]
