# Title: Flip Columns For Maximum Number of Equal Rows
# URL: https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
# Difficulty: Medium

from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_frequency = {}
        for row in matrix:
            pattern = tuple(row)
            if pattern not in pattern_frequency:
                pattern_frequency[pattern] = 0
            pattern_frequency[pattern] += 1

            flipped_pattern = tuple([1 - x for x in row])
            if flipped_pattern not in pattern_frequency:
                pattern_frequency[flipped_pattern] = 0
            pattern_frequency[flipped_pattern] += 1

        return max(pattern_frequency.values()) if pattern_frequency else 0


class TestMaxEqualRowsAfterFlips:
    def test_example1(self):
        matrix = [[0, 1], [1, 1]]
        expected = 1
        solution = Solution()
        assert solution.maxEqualRowsAfterFlips(matrix) == expected

    def test_example2(self):
        matrix = [[0, 1], [1, 0]]
        expected = 2
        solution = Solution()
        assert solution.maxEqualRowsAfterFlips(matrix) == expected

    def test_example3(self):
        matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
        expected = 2
        solution = Solution()
        assert solution.maxEqualRowsAfterFlips(matrix) == expected
