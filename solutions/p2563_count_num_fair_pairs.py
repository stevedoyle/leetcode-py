# Title: Count Number of Fair Pairs
# URL: https://leetcode.com/problems/count-number-of-fair-pairs/
# Difficulty: Medium

from typing import List


class Solution:
    # Time Complexity: O(nlogn), where n is the length of nums.
    # Space Complexity: O(1).
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        result = 0
        while left < right:
            sum = nums[left] + nums[right]
            if sum < target:
                result += right - left
                left += 1
            else:
                right -= 1
        return result

    # Time Complexity: O(n^2), where n is the length of nums.
    # Space Complexity: O(1).
    def countFairPairsV2(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] >= lower and nums[i] + nums[j] <= upper:
                    count += 1

        return count


class TestCountFairPairs:
    def test_example1(self):
        nums = [0, 1, 7, 4, 4, 5]
        lower = 3
        upper = 6
        expected = 6
        assert Solution().countFairPairs(nums, lower, upper) == expected
        assert Solution().countFairPairsV2(nums, lower, upper) == expected

    def test_example2(self):
        nums = [1, 7, 9, 2, 5]
        lower = 11
        upper = 11
        expected = 1
        assert Solution().countFairPairs(nums, lower, upper) == expected
        assert Solution().countFairPairsV2(nums, lower, upper) == expected
