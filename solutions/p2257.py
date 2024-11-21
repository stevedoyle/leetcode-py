# Title: Count Unguarded Cells in the Grid
# URL: https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
# Difficulty: Medium

from typing import List


class Solution:
    UNGUARDED = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3

    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[self.UNGUARDED] * n for _ in range(m)]

        for wall in walls:
            x, y = wall
            grid[x][y] = self.WALL

        for guard in guards:
            x, y = guard
            grid[x][y] = self.GUARD

        # Horizontal passes
        for row in range(m):
            is_guard_line_active = grid[row][0] == self.GUARD
            for col in range(n):
                is_guard_line_active = self.updateCellVisibility(
                    grid, row, col, is_guard_line_active
                )
            is_guard_line_active = grid[row][n - 1] == self.GUARD
            for col in range(n - 2, -1, -1):
                is_guard_line_active = self.updateCellVisibility(
                    grid, row, col, is_guard_line_active
                )

        # Vertical passes
        for col in range(n):
            is_guard_line_active = grid[0][col] == self.GUARD
            for row in range(m):
                is_guard_line_active = self.updateCellVisibility(
                    grid, row, col, is_guard_line_active
                )
            is_guard_line_active = grid[m - 1][col] == self.GUARD
            for row in range(m - 2, -1, -1):
                is_guard_line_active = self.updateCellVisibility(
                    grid, row, col, is_guard_line_active
                )

        # Count unguarded cells
        unguarded = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.UNGUARDED:
                    unguarded += 1
        return unguarded

    def updateCellVisibility(self, grid, row, col, is_guard_line_active):
        if grid[row][col] == self.GUARD:
            return True

        if grid[row][col] == self.WALL:
            return False

        if is_guard_line_active:
            grid[row][col] = self.GUARDED
        return is_guard_line_active


class TestCountUnguarded:
    def test_example1(self):
        m = 4
        n = 6
        guards = [[0, 0], [1, 1], [2, 3]]
        walls = [[0, 1], [2, 2], [1, 4]]
        expected = 7
        assert Solution().countUnguarded(m, n, guards, walls) == expected

    def test_example2(self):
        m = 3
        n = 3
        guards = [[1, 1]]
        walls = [[0, 1], [1, 0], [2, 1], [1, 2]]
        expected = 4
        assert Solution().countUnguarded(m, n, guards, walls) == expected
