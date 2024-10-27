# Title: Contains Duplicate II
# URL: https://leetcode.com/problems/contains-duplicate-ii/
# Difficulty: Easy

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_index = set()

        for i, num in enumerate(nums):
            if num in num_index:
                return True

            num_index.add(num)

            if len(num_index) > k:
                # Remove the oldest number
                num_index.remove(nums[i - k])

        return False


class TestContainsNearlyDuplicate:
    def test_example1(self):
        nums = [1, 2, 3, 1]
        k = 3
        assert Solution().containsNearbyDuplicate(nums, k)

    def test_example2(self):
        nums = [1, 0, 1, 1]
        k = 1
        assert Solution().containsNearbyDuplicate(nums, k)

    def test_example3(self):
        nums = [1, 2, 3, 1, 2, 3]
        k = 2
        assert not Solution().containsNearbyDuplicate(nums, k)
