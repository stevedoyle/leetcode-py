# Title: Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        k = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[k]:
                k += 1
                nums[k] = nums[j]
        return k + 1


class TestRemoveDuplicates:
    def test_example1(self):
        nums = [1, 1, 2]
        assert Solution().removeDuplicates(nums) == 2
        assert nums[:2] == [1, 2]

    def test_example2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        assert Solution().removeDuplicates(nums) == 5
        assert nums[:5] == [0, 1, 2, 3, 4]
