# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from utils import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class TestIsSameTree:
    def test_example1(self):
        p = [1, 2, 3]
        q = [1, 2, 3]
        tree1 = TreeNode.from_list(p)
        tree2 = TreeNode.from_list(q)
        expected = True
        result = Solution().isSameTree(tree1, tree2)  # type: ignore
        assert result == expected

    def test_example2(self):
        p = [1, 2]
        q = [1, None, 2]
        tree1 = TreeNode.from_list(p)
        tree2 = TreeNode.from_list(q)
        expected = False
        result = Solution().isSameTree(tree1, tree2)  # type: ignore
        assert result == expected

    def test_example3(self):
        p = [1, 2, 1]
        q = [1, 1, 2]
        tree1 = TreeNode.from_list(p)
        tree2 = TreeNode.from_list(q)
        expected = False
        result = Solution().isSameTree(tree1, tree2)  # type: ignore
        assert result == expected
