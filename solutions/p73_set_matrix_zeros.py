# Title: Set Matrix Zeroes
# URL: https://leetcode.com/problems/set-matrix-zeroes/
# Difficulty: Medium

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrows, ncols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in range(nrows):
            for j in range(ncols):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0


class TestSetZeroes:
    def test_example1(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        Solution().setZeroes(matrix)
        assert matrix == expected

    def test_example2(self):
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        Solution().setZeroes(matrix)
        assert matrix == expected
