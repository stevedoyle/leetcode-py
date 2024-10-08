# Title: Number of Islands
# URL: https://leetcode.com/problems/number-of-islands/
# Difficulty: Medium

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = []
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    queue.append((i, j))
                    count += 1
                    while queue:
                        x, y = queue.pop(0)
                        if (
                            x < 0
                            or y < 0
                            or x >= len(grid)
                            or y >= len(grid[0])
                            or grid[x][y] == "0"
                        ):
                            continue
                        grid[x][y] = "0"
                        queue.append((x + 1, y))
                        queue.append((x - 1, y))
                        queue.append((x, y + 1))
                        queue.append((x, y - 1))
        return count


class TestNumIslands:
    def test_example1(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        assert Solution().numIslands(grid) == 1

    def test_example2(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        assert Solution().numIslands(grid) == 3
