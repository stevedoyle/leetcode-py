# Title: Longest Consecutive Sequence
# URL: https://leetcode.com/problems/longest-consecutive-sequence/
# Difficulty: Medium

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(list(set(nums)))
        max_streak = 0

        previous_num = nums[0]
        streak = 1
        for num in nums[1:]:
            if previous_num is None:
                previous_num = num
                streak = 1
                continue
            if num == previous_num + 1:
                streak += 1
            else:
                max_streak = max(max_streak, streak)
                streak = 1
            previous_num = num
        return max(max_streak, streak)


class TestLongestConsecutive:
    def test_example1(self):
        nums = [100, 4, 200, 1, 3, 2]
        expected = 4
        assert Solution().longestConsecutive(nums) == expected

    def test_example2(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        expected = 9
        assert Solution().longestConsecutive(nums) == expected
