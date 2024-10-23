# Title: 2461. Cousins in Binary Tree II
# URL: https://leetcode.com/problems/cousins-in-binary-tree-ii/
# Difficulty: Medium

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_list(self) -> list:
        result = []
        queue = [self]
        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.val)
                if current.left or current.right:
                    queue.append(current.left)
                    queue.append(current.right)
            else:
                result.append(None)
        return result


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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = [root]
        level_sums = []

        # First BFS: Calculate sum of nodes at each level
        while queue:
            level_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                current = queue.pop(0)
                level_sum += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            level_sums.append(level_sum)

        # Second BFS: Update each node's value to sum of its cousins
        queue.append(root)
        level_index = 1
        root.val = 0  # Root has no cousins
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                current = queue.pop(0)

                sibling_sum = (current.left.val if current.left else 0) + (
                    current.right.val if current.right else 0
                )

                if current.left:
                    current.left.val = level_sums[level_index] - sibling_sum
                    queue.append(current.left)
                if current.right:
                    current.right.val = level_sums[level_index] - sibling_sum
                    queue.append(current.right)
            level_index += 1

        return root


class TestSolution:
    def test_example1(self):
        root = create_tree([5, 4, 9, 1, 10, None, 7])
        expected = [0, 0, 0, 7, 7, None, 11]
        assert Solution().replaceValueInTree(root).to_list() == expected

    def test_example2(self):
        root = create_tree([3, 1, 2])
        expected = [0, 0, 0]
        assert Solution().replaceValueInTree(root).to_list() == expected
