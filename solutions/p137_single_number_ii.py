# Title: Single Number II
# URL: https://leetcode.com/problems/single-number-ii/
# Difficulty: Medium

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        msb, lsb = 0, 0
        for num in nums:
            lsb = ~msb & (lsb ^ num)
            msb = ~lsb & (msb ^ num)
        return lsb

    # Time complexity: O(n)
    # Space complexity: O(n)
    def singleNumber2(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2


class TestSingleNumber:
    def test_example1(self):
        nums = [2, 2, 3, 2]
        assert Solution().singleNumber(nums) == 3

    def test_example2(self):
        nums = [0, 1, 0, 1, 0, 1, 99]
        assert Solution().singleNumber(nums) == 99

    def test_example1_v2(self):
        nums = [2, 2, 3, 2]
        assert Solution().singleNumber2(nums) == 3

    def test_example2_v2(self):
        nums = [0, 1, 0, 1, 0, 1, 99]
        assert Solution().singleNumber2(nums) == 99
