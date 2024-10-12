# Title: Clone Graph
# URL: https://leetcode.com/problems/clone-graph/
# Difficulty: Medium

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from utils import Node
from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return node
        visited = {}

        def dfs(node):
            if node.val in visited:
                return visited[node.val]
            clone = Node(node.val)
            visited[node.val] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)


class TestCloneGraph:
    def test_example1(self):
        input = Node.from_list([[2, 4], [1, 3], [2, 4], [1, 3]])
        expected = [[2, 4], [1, 3], [2, 4], [1, 3]]
        result = Solution().cloneGraph(input)
        result = result.to_list() if result else None
        assert result == expected

    def test_example2(self):
        input = Node.from_list([[]])
        expected = [[]]
        result = Solution().cloneGraph(input)
        result = result.to_list() if result else []
        assert result == expected

    def test_example3(self):
        input = Node.from_list([])
        expected = []
        result = Solution().cloneGraph(input)
        result = result.to_list() if result else []
        assert result == expected
