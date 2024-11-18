# Title: Rotate Image
# URL: https://leetcode.com/problems/rotate-image/
# Difficulty: Medium

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrows, ncols = len(matrix), len(matrix[0])
        rotated = [[0] * ncols for _ in range(nrows)]
        for i in range(nrows):
            for j in range(ncols):
                rotated[j][nrows - i - 1] = matrix[i][j]
        for i in range(nrows):
            for j in range(ncols):
                matrix[i][j] = rotated[i][j]


class TestRotate:
    def test_example1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        Solution().rotate(matrix)
        assert matrix == expected

    def test_example2(self):
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        expected = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        Solution().rotate(matrix)
        assert matrix == expected
