# Title: Minimum Number of Removals to Make Mountain Array
# URL: https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/
# Difficulty: Hard

from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        for i in range(n):
            left[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    left[i] = max(left[i], left[j] + 1)
        for i in range(n - 1, -1, -1):
            right[i] = 1
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    right[i] = max(right[i], right[j] + 1)
        ans = 0
        for i in range(1, n - 1):
            if left[i] > 1 and right[i] > 1:
                ans = max(ans, left[i] + right[i] - 1)
        return n - ans if ans > 0 else 0


class TestMinRemovals:
    def test_example1(self):
        nums = [1, 3, 1]
        expected = 0
        assert Solution().minimumMountainRemovals(nums) == expected

    def test_example2(self):
        nums = [2, 1, 1, 5, 6, 2, 3, 1]
        expected = 3
        assert Solution().minimumMountainRemovals(nums) == expected
