# Title: Find the Power of K-Size Subarrays I
# URL: https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/
# Difficulty: Medium

from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []

        return [self.power(nums[i : i + k]) for i in range(len(nums) - k + 1)]

    def power(self, nums: List[int]) -> int:
        if not nums:
            return -1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                return -1

        return nums[-1]


class TestResultsArray:
    def test_example1(self):
        nums = [1, 2, 3, 4, 3, 2, 5]
        k = 3
        expected = [3, 4, -1, -1, -1]
        assert Solution().resultsArray(nums, k) == expected

    def test_example2(self):
        nums = [2, 2, 2, 2, 2]
        k = 4
        expected = [-1, -1]
        assert Solution().resultsArray(nums, k) == expected

    def test_example3(self):
        nums = [3, 2, 3, 2, 3, 2]
        k = 2
        expected = [-1, 3, -1, 3, -1]
        assert Solution().resultsArray(nums, k) == expected

    def test_power(self):
        assert Solution().power([1, 2, 3, 4, 5]) == 5
        assert Solution().power([1, 2, 3, 4, 4]) == -1
