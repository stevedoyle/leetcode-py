# Title: Next Permutation
# URL: https://leetcode.com/problems/next-permutation/
# Difficulty: Medium

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i + 1)

    def reverse(self, nums, start):
        # swap the order of the elements from start to the end
        i, j = start, len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1

    def swap(self, nums, i, j):
        # swap two elements in the list
        nums[i], nums[j] = nums[j], nums[i]


class TestNextPermutation:
    def test_example1(self):
        nums = [1, 2, 3]
        Solution().nextPermutation(nums)
        assert nums == [1, 3, 2]

    def test_example2(self):
        nums = [3, 2, 1]
        Solution().nextPermutation(nums)
        assert nums == [1, 2, 3]

    def test_example3(self):
        nums = [1, 1, 5]
        Solution().nextPermutation(nums)
        assert nums == [1, 5, 1]
