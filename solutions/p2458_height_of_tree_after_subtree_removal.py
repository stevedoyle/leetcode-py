# Title: Height of Binary Tree After Subtree Removal Queries
# URL: https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/
# Difficulty: Hard

from typing import List, Optional
from utils import TreeNode, create_tree


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        result_map = {}
        height_cache = {}

        def height(node):
            if not node:
                return -1

            if node.val in height_cache:
                return height_cache[node.val]

            h = 1 + max(height(node.left), height(node.right))
            height_cache[node.val] = h
            return h

        # DFS to precompute the amx  value after removing the subtree
        def dfs(node, depth, max_val):
            if not node:
                return

            result_map[node.val] = max_val
            dfs(node.left, depth + 1, max(max_val, depth + 1 + height(node.right)))
            dfs(node.right, depth + 1, max(max_val, depth + 1 + height(node.left)))

        dfs(root, 0, 0)
        return [result_map[q] for q in queries]


class TestTreeQueries:
    def test_example1(self):
        root = create_tree([1, 3, 4, 2, None, 6, 5, None, None, None, None, None, 7])
        queries = [4]
        assert Solution().treeQueries(root, queries) == [2]

    def test_example2(self):
        root = create_tree([5, 8, 9, 2, 1, 3, 7, 4, 6])
        queries = [3, 2, 4, 8]
        assert Solution().treeQueries(root, queries) == [3, 2, 3, 2]

    def test_example3(self):
        root = create_tree([1, None, 5, 3, None, 2, 4])
        queries = [3, 5, 4, 2, 4]
        assert Solution().treeQueries(root, queries) == [1, 0, 3, 3, 3]
