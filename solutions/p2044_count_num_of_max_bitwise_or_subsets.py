# Title: Count Number of Maximum Bitwise-OR Subsets
# URL: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
# Difficulty: Medium

from typing import List
from functools import reduce


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        n = len(nums)

        # Calculate the maximum bitwise OR
        max_or = reduce(lambda x, y: x | y, nums)

        # Initialize memo with -1
        memo = [[-1] * (max_or + 1) for _ in range(n)]

        return self._countMaxOrSubsetsRecursive(nums, 0, 0, max_or, memo)

    def _countMaxOrSubsetsRecursive(self, nums, idx, current_or, target_or, memo):
        if idx == len(nums):
            return 1 if current_or == target_or else 0

        # Check if the result is already memoized
        if memo[idx][current_or] != -1:
            return memo[idx][current_or]

        # Don't include the current number
        count = self._countMaxOrSubsetsRecursive(
            nums, idx + 1, current_or, target_or, memo
        )

        # Include the current number
        count += self._countMaxOrSubsetsRecursive(
            nums, idx + 1, current_or | nums[idx], target_or, memo
        )

        # Memoize the result
        memo[idx][current_or] = count
        return memo[idx][current_or]


class TestCountMaxOrSubsets:
    def test_example1(self):
        nums = [3, 1]
        expected = 2
        assert Solution().countMaxOrSubsets(nums) == expected

    def test_example2(self):
        nums = [2, 2, 2]
        expected = 7
        assert Solution().countMaxOrSubsets(nums) == expected

    def test_example3(self):
        nums = [3, 2, 1, 5]
        expected = 6
        assert Solution().countMaxOrSubsets(nums) == expected
