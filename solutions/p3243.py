# Title: Shortest Distance After Road Addition Queries I
# URL: https://binarysearch.com/problems/Shortest-Distance-After-Road-Addition-Queries-I
# Difficulty: Medium

from typing import List


class Solution:
    def find_min_distance(self, adj_list, n):
        dp = [0] * n
        dp[n - 1] = 0  # Base case

        for current_node in range(n - 2, -1, -1):
            min_distance = n
            for neighbor in adj_list[current_node]:
                min_distance = min(min_distance, dp[neighbor] + 1)
            dp[current_node] = min_distance

        return dp[0]

    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        answer = []
        adj_list = [[] for _ in range(n)]

        for i in range(n):
            adj_list[i].append(i + 1)

        for road in queries:
            u, v = road[0], road[1]
            adj_list[u].append(v)

            answer.append(self.find_min_distance(adj_list, n))

        return answer


class TestShortestDistanceAfterQueries:
    def test_example1(self):
        n = 5
        queries = [[2, 4], [0, 2], [0, 4]]
        expected = [3, 2, 1]
        assert Solution().shortestDistanceAfterQueries(n, queries) == expected

    def test_example2(self):
        n = 4
        queries = [[0, 3], [0, 2]]
        expected = [1, 1]
        assert Solution().shortestDistanceAfterQueries(n, queries) == expected
