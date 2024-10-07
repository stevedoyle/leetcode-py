# Title: Search in Rotated Sorted Array
# URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Difficulty: Medium

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the pivot index using a binary search
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left

        # Find the target index using a binary search
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[(mid + pivot) % len(nums)]
            if mid_val == target:
                return (mid + pivot) % len(nums)
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


class TestSearch:
    def test_example1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        assert Solution().search(nums, target) == 4

    def test_example2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        assert Solution().search(nums, target) == -1

    def test_example3(self):
        nums = [1]
        target = 0
        assert Solution().search(nums, target) == -1
