# Title: 209. Minimum Size Subarray Sum
# URL: https://leetcode.com/problems/minimum-size-subarray-sum/
# Difficulty: Medium

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sum = 0
        min_length = float("inf")

        while right < len(nums):
            sum += nums[right]
            right += 1

            while sum >= target:
                min_length = min(min_length, right - left)
                sum -= nums[left]
                left += 1

        return min_length if min_length != float("inf") else 0


class TestMinSubArrayLen:
    def test_example1(self):
        target = 7
        nums = [2, 3, 1, 2, 4, 3]
        assert Solution().minSubArrayLen(target, nums) == 2

    def test_example2(self):
        target = 4
        nums = [1, 4, 4]
        assert Solution().minSubArrayLen(target, nums) == 1

    def test_example3(self):
        target = 11
        nums = [1, 1, 1, 1, 1, 1, 1, 1]
        assert Solution().minSubArrayLen(target, nums) == 0
