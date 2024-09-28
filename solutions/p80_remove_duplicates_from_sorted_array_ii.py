# Title: Remove Duplicates from Sorted Array II
# url: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Difficulty: Medium


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)

        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1

        return i


class TestRemoveDuplicates:
    def test_example1(self):
        nums = [1, 1, 1, 2, 2, 3]
        expected = 5

        solution = Solution()
        assert solution.removeDuplicates(nums) == expected

    def test_example2(self):
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        expected = 7

        solution = Solution()
        assert solution.removeDuplicates(nums) == expected

    def test_example3(self):
        nums = [1, 1, 1]
        expected = 2

        solution = Solution()
        assert solution.removeDuplicates(nums) == expected

    def test_example4(self):
        nums = [1, 1, 1, 1]
        expected = 2

        solution = Solution()
        assert solution.removeDuplicates(nums) == expected
