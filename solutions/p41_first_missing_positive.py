# Link: https://leetcode.com/problems/first-missing-positive/
# Difficulty: Hard

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def firstMissingPositiveUnoptimized(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        i = 1
        while i in uniqueNums:
            i += 1
        return i

    # Optimized solution
    # Time complexity: O(n)
    # Space complexity: O(1)
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return nums[-1] + 1


# Test cases
class TestFirstMissingPositive:
    def test_first_missing_positive(self):
        solution = Solution()
        assert solution.firstMissingPositive([1, 2, 0]) == 3
        assert solution.firstMissingPositive([3, 4, -1, 1]) == 2
        assert solution.firstMissingPositive([7, 8, 9, 11, 12]) == 1
        assert solution.firstMissingPositive([1]) == 2

    def test_first_missing_positive_unoptimized(self):
        solution = Solution()
        assert solution.firstMissingPositiveUnoptimized([1, 2, 0]) == 3
        assert solution.firstMissingPositiveUnoptimized([3, 4, -1, 1]) == 2
        assert solution.firstMissingPositiveUnoptimized([7, 8, 9, 11, 12]) == 1
        assert solution.firstMissingPositiveUnoptimized([1]) == 2
