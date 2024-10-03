# Title: Make Sum Divisible by P
# URL: https://leetcode.com/problems/make-sum-divisible-by-p/
# Difficulty: Medium
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums) % p == 0:
            return 0

        n = len(nums)
        target = sum(nums) % p
        prefix_sum = 0
        prefix_sums = {0: -1}
        min_length = n
        current_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            prefix_sums[prefix_sum % p] = i
            current_sum = (current_sum + num) % p
            if (current_sum - target) % p in prefix_sums:
                min_length = min(
                    min_length, i - prefix_sums[(current_sum - target) % p]
                )

        return min_length if min_length < n else -1


class TestMinSubArray:
    def test_example1(self):
        nums = [3, 1, 4, 2]
        p = 6
        assert Solution().minSubarray(nums, p) == 1

    def test_example2(self):
        nums = [6, 3, 5, 2]
        p = 9
        assert Solution().minSubarray(nums, p) == 2

    def test_example3(self):
        nums = [1, 2, 3]
        p = 3
        assert Solution().minSubarray(nums, p) == 0
