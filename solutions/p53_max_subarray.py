# Title: Maximum Subarray
# URL: https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medum

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = best_sum = -float("inf")
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum


class TestMaxSubarray:
    def test_example1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected = 6
        assert Solution().maxSubArray(nums) == expected

    def test_example2(self):
        nums = [1]
        expected = 1
        assert Solution().maxSubArray(nums) == expected

    def test_example3(self):
        nums = [5, 4, -1, 7, 8]
        expected = 23
        assert Solution().maxSubArray(nums) == expected

    def test_example4(self):
        nums = [-1]
        expected = -1
        assert Solution().maxSubArray(nums) == expected
