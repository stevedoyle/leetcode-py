# Title: Count Square Submatrices with All Ones
# URL: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# Difficulty: Medium

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        count = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 1:
                    if row == 0 or col == 0:
                        count += 1
                    else:
                        matrix[row][col] = (
                            min(
                                matrix[row - 1][col],
                                matrix[row][col - 1],
                                matrix[row - 1][col - 1],
                            )
                            + 1
                        )
                        count += matrix[row][col]
        return count


class TestCountSquares:
    def test_example1(self):
        input = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
        expected = 15
        assert Solution().countSquares(input) == expected

    def test_example2(self):
        input = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
        expected = 7
        assert Solution().countSquares(input) == expected
