# Title: Single Number
# URL: https://leetcode.com/problems/single-number/
# Difficulty: Easy

from typing import List
import functools


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return functools.reduce(lambda x, y: x ^ y, nums)


class TestSingleNumber:
    def test_example1(self):
        nums = [2, 2, 1]
        assert Solution().singleNumber(nums) == 1

    def test_example2(self):
        nums = [4, 1, 2, 1, 2]
        assert Solution().singleNumber(nums) == 4

    def test_example3(self):
        nums = [1]
        assert Solution().singleNumber(nums) == 1
