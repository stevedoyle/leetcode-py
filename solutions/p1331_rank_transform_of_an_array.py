# Title: Rank Transform of an Array
# URL: https://leetcode.com/problems/rank-transform-of-an-array/
# Difficulty: Easy

from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for i, num in enumerate(sorted(set(arr))):
            rank[num] = i + 1

        return [rank[num] for num in arr]


class TestArrayRankTransform:
    def test_example1(self):
        arr = [40, 10, 20, 30]
        expected = [4, 1, 2, 3]

        solution = Solution()
        assert solution.arrayRankTransform(arr) == expected

    def test_example2(self):
        arr = [100, 100, 100]
        expected = [1, 1, 1]

        solution = Solution()
        assert solution.arrayRankTransform(arr) == expected

    def test_example3(self):
        arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
        expected = [5, 3, 4, 2, 8, 6, 7, 1, 3]

        solution = Solution()
        assert solution.arrayRankTransform(arr) == expected
