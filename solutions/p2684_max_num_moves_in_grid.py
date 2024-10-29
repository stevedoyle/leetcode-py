# Title: Maximum Number of Moves in a Grid
# URL: https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/
# Difficulty: Medium

from typing import List


class Solution:
    dirs = [-1, 0, 1]

    def DFS(self, row, col, grid, dp):
        M, N = len(grid), len(grid[0])
        if dp[row][col] != -1:
            return dp[row][col]

        max_moves = 0
        for dir in self.dirs:
            new_row, new_col = row + dir, col + 1
            if (
                0 <= new_row < M
                and 0 <= new_col < N
                and grid[new_row][new_col] > grid[row][col]
            ):
                max_moves = max(max_moves, 1 + self.DFS(new_row, new_col, grid, dp))

        dp[row][col] = max_moves
        return max_moves

    def maxMoves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[-1] * N for _ in range(M)]
        max_moves = 0

        for row in range(M):
            moves_required = self.DFS(row, 0, grid, dp)
            max_moves = max(max_moves, moves_required)

        return max_moves


class TestMaxMoves:
    def test_example1(self):
        grid = [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]
        assert Solution().maxMoves(grid) == 3

    def test_example2(self):
        grid = [[3, 2, 4], [2, 1, 9], [1, 1, 7]]
        assert Solution().maxMoves(grid) == 0
