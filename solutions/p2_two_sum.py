# Title: Two Sum
# URL: https://leetcode.com/problems/two-sum/
# Difficulty: Easy

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            if target - num in map:
                return [map[target - num], i]
            map[num] = i
        return []


class TestTwoSum:
    def test_one(self):
        nums = [2, 7, 11, 15]
        target = 9
        assert Solution().twoSum(nums, target) == [0, 1]

    def test_two(self):
        nums = [3, 2, 4]
        target = 6
        assert Solution().twoSum(nums, target) == [1, 2]

    def test_three(self):
        nums = [3, 3]
        target = 6
        assert Solution().twoSum(nums, target) == [0, 1]
