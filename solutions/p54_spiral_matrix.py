# Title: Spiral Matrix
# URL: https://leetcode.com/problems/spiral-matrix/
# Difficulty: Medium

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        row_start, row_end = 0, len(matrix)
        col_start, col_end = 0, len(matrix[0])
        result = []

        while row_start < row_end and col_start < col_end:
            result.extend(matrix[row_start][col_start:col_end])
            row_start += 1
            result.extend([matrix[i][col_end - 1] for i in range(row_start, row_end)])
            col_end -= 1
            if row_start < row_end:
                result.extend(matrix[row_end - 1][col_start:col_end][::-1])
            row_end -= 1
            if col_start < col_end:
                result.extend(
                    [matrix[i][col_start] for i in range(row_start, row_end)][::-1]
                )
            col_start += 1

        print(result)
        return result


class TestSpiralOrder:
    def test_example1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        assert Solution().spiralOrder(matrix) == expected

    def test_example2(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        assert Solution().spiralOrder(matrix) == expected
