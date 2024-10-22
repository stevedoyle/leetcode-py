# Title: Kth Largest Sum in a Binary Tree
# URL: https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/
# Difficulty: Medium

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(arr: list) -> Optional[TreeNode]:
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        current = queue.pop(0)
        if arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1
    return root


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        sums = []

        def dfs(node, level):
            if not node:
                return
            if level >= len(sums):
                sums.append(0)
            sums[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        sums.sort(reverse=True)
        return sums[k - 1] if k <= len(sums) else -1


class TestKthLargestLevelSum:
    def test_example1(self):
        root = create_tree([5, 8, 9, 2, 1, 3, 7, 4, 6])
        k = 2
        expected = 13
        assert Solution().kthLargestLevelSum(root, k) == expected

    def test_example2(self):
        root = create_tree([1, 2, None, 3])
        k = 1
        expected = 3
        assert Solution().kthLargestLevelSum(root, k) == expected

    def test_example3(self):
        root = create_tree([5, 8, 9, 2, 1, 3, 7])
        k = 4
        expexted = -1
        assert Solution().kthLargestLevelSum(root, k) == expexted
