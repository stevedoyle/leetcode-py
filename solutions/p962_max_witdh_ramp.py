# Title: 962. Maximum Width Ramp
# URL: https://leetcode.com/problems/maximum-width-ramp/
# Difficulty: Medium

from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        ans = 0
        for i in reversed(range(n)):
            while stack and nums[i] >= nums[stack[-1]]:
                ans = max(ans, i - stack.pop())
        return ans


class TestMaxWidthRamp:
    def test_example1(self):
        nums = [6, 0, 8, 2, 1, 5]
        assert Solution().maxWidthRamp(nums) == 4

    def test_example2(self):
        nums = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
        assert Solution().maxWidthRamp(nums) == 7
