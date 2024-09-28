# Title: Minimum Element After Decrementing and Rearranging
# URL: https://leetcode.com/problems/minimum-element-after-decrementing-and-rearranging/
# Difficulty: Easy

from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_element = nums[0]
        for num in nums:
            digit_sum = sumOfDigits(num)
            if digit_sum < min_element:
                min_element = digit_sum
        return min_element


def sumOfDigits(num: int) -> int:
    return sum([int(digit) for digit in str(num)])


class TestMinElement:
    def test_example1(self):
        nums = [10, 12, 13, 14]
        assert Solution().minElement(nums) == 1

    def test_example2(self):
        nums = [1, 2, 3, 4]
        assert Solution().minElement(nums) == 1

    def test_example3(self):
        nums = [999, 19, 199]
        assert Solution().minElement(nums) == 10

    def test_sumOfDigits(self):
        assert sumOfDigits(10) == 1
        assert sumOfDigits(12) == 3
        assert sumOfDigits(13) == 4
        assert sumOfDigits(14) == 5
        assert sumOfDigits(999) == 27
        assert sumOfDigits(19) == 10
        assert sumOfDigits(199) == 19
