# Title: Remove Element
# URL: https://leetcode.com/problems/remove-element/
# Difficulty: Easy

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # index of the next element to be replaced
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


class TestRemoveElement:
    def test_example1(self):
        nums = [3, 2, 2, 3]
        assert Solution().removeElement(nums, 3) == 2

    def test_example2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        assert Solution().removeElement(nums, 2) == 5
