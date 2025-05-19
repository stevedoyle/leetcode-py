# Title: Maximum Sum of a Pair With Equal Sum of Digits
# URL: https://leetcode.com/problems/maximum-sum-of-a-pair-with-equal-sum-of-digits/
# Difficulty: Medium

from typing import List
from collections import defaultdict


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_map = defaultdict(int)
        max_sum = -1

        for num in nums:
            digit_sum = self.get_digit_sum(num)
            if digit_sum in digit_sum_map:
                max_sum = max(max_sum, num + digit_sum_map[digit_sum])

            digit_sum_map[digit_sum] = max(digit_sum_map[digit_sum], num)

        return max_sum

    def get_digit_sum(self, num: int) -> int:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum


class TestMaximumSum:
    def test_example1(self):
        nums = [18, 43, 36, 13, 7]
        expected = 54
        s = Solution()
        result = s.maximumSum(nums)
        assert result == expected

    def test_example2(self):
        nums = [10, 12, 19, 14]
        expected = -1
        s = Solution()
        result = s.maximumSum(nums)
        assert result == expected
