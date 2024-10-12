# Title: Target Sum
# URL: https://leetcode.com/problems/target-sum/
# Difficulty: Medium

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(index, target):
            if index == len(nums):
                return 1 if target == 0 else 0

            if (index, target) in memo:
                return memo[(index, target)]

            positive = dfs(index + 1, target - nums[index])
            negative = dfs(index + 1, target + nums[index])

            memo[(index, target)] = positive + negative

            return memo[(index, target)]

        memo = {}
        return dfs(0, target)


class TestTargetSum:
    def test_example1(self):
        nums = [1, 1, 1, 1, 1]
        target = 3
        assert Solution().findTargetSumWays(nums, target) == 5

    def test_example2(self):
        nums = [1]
        target = 1
        assert Solution().findTargetSumWays(nums, target) == 1
