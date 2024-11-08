# Title: 198. House Robber
# URL: https://leetcode.com/problems/house-robber/
# Difficulty: Medium

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        max_amount = [0] * (n + 1)

        max_amount[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            max_amount[i] = max(max_amount[i + 1], nums[i] + max_amount[i + 2])

        return max_amount[0]


class TestRob:
    def test_example1(self):
        nums = [1, 2, 3, 1]
        assert Solution().rob(nums) == 4

    def test_example2(self):
        nums = [2, 7, 9, 3, 1]
        assert Solution().rob(nums) == 12
