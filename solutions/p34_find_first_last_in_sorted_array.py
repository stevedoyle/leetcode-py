# Title: Find First and Last Position of Element in Sorted Array
# URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Difficulty: Medium

from typing import List


class Solution:
    # Runtime complexity: O(log n)
    # Space complexity: O(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, lower):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target or (lower and target == nums[mid]):
                    right = mid
                else:
                    left = mid + 1
            return left

        leftIdx = binarySearch(nums, target, True)
        if leftIdx == len(nums) or nums[leftIdx] != target:
            return [-1, -1]
        return [leftIdx, binarySearch(nums, target, False) - 1]


class TestSearchInSortedArray:
    def test_example1(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        output = [3, 4]
        assert Solution().searchRange(nums, target) == output

    def test_example2(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        output = [-1, -1]
        assert Solution().searchRange(nums, target) == output

    def test_example3(self):
        nums = []
        target = 0
        output = [-1, -1]
        assert Solution().searchRange(nums, target) == output
