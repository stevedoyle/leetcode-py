# 2352. Equal Row and Column Pairs
# URL: https://leetcode.com/problems/equal-row-and-column-pairs/
# Difficulty: Medium


from typing import List
from collections import defaultdict


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def to_key(arr):
            return tuple(arr)

        row_map = defaultdict(int)
        col_map = defaultdict(int)
        n = len(grid)
        count = 0

        for i in range(n):
            row_map[to_key(tuple(grid[i]))] += 1
            col_map[to_key(tuple(grid[j][i] for j in range(n)))] += 1

        for row in row_map:
            if row in col_map:
                count += row_map[row] * col_map[row]

        return count


class TestEqualPairs:
    def test_example1(self):
        grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
        expected = 1
        s = Solution()
        result = s.equalPairs(grid)
        assert result == expected

    def test_example2(self):
        grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
        expected = 3
        s = Solution()
        result = s.equalPairs(grid)
        assert result == expected
