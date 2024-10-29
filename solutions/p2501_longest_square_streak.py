# Title: Longest Square Streak in an Array
# URL: https://leetcode.com/problems/longest-square-streak-in-an-array/
# Difficulty: Medium

from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        streak_lengths = {}
        nums.sort()

        for number in nums:
            root = int(number**0.5)

            if root * root == number and root in streak_lengths:
                streak_lengths[number] = streak_lengths[root] + 1
            else:
                streak_lengths[number] = 1

        longest_streak = max(streak_lengths.values(), default=0)

        return longest_streak if longest_streak > 1 else -1


class TestLongestSquareStreak:
    def test_example1(self):
        nums = [4, 3, 6, 16, 8, 2]
        expected = 3
        assert Solution().longestSquareStreak(nums) == expected

    def test_example2(self):
        nums = [2, 3, 5, 6, 7]
        expected = -1
        assert Solution().longestSquareStreak(nums) == expected
