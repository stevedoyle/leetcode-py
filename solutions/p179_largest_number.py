# Title: Largest Number
# URL: https://leetcode.com/problems/largest-number/
# Difficulty: Medium

from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(x + y) - int(y + x)

        sorted_nums = sorted(map(str, nums), key=cmp_to_key(compare), reverse=True)
        return str(int("".join(sorted_nums)))

    def largestNumber2(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(x + y) - int(y + x)

        sorted_nums = sorted(map(str, nums), key=cmp_to_key(compare), reverse=True)
        return str(int("".join(sorted_nums)))


class TestLargestNumber:
    def test_example1(self):
        nums = [10, 2]
        expected = "210"
        assert Solution().largestNumber(nums) == expected
        assert Solution().largestNumber2(nums) == expected

    def test_example2(self):
        nums = [3, 30, 34, 5, 9]
        expected = "9534330"
        assert Solution().largestNumber(nums) == expected
        assert Solution().largestNumber2(nums) == expected
