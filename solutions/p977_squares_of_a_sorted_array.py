# Title: Squares of a Sorted Array
# URL: https://leetcode.com/problems/squares-of-a-sorted-array/
# Difficulty: Easy

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x**2 for x in nums])


class TestSortedSquares:
    def test_example1(self):
        nums = [-4, -1, 0, 3, 10]
        expected = [0, 1, 9, 16, 100]
        assert Solution().sortedSquares(nums) == expected

    def test_example2(self):
        nums = [-7, -3, 2, 3, 11]
        expected = [4, 9, 9, 49, 121]
        assert Solution().sortedSquares(nums) == expected
