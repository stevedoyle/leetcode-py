# Title: 57. Insert Interval
# URL: https://leetcode.com/problems/insert-interval/
# Difficulty: Medium

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals

        left, right = newInterval
        left_idx = 0
        right_idx = 0
        n = len(intervals)
        for i in range(n):
            if left <= intervals[i][1]:
                left_idx = i
                break
            left_idx = i + 1
        for i in range(n):
            if right < intervals[i][0]:
                right_idx = i
                break
            right_idx = i + 1
        if left_idx == right_idx:
            return intervals[:left_idx] + [newInterval] + intervals[right_idx:]
        new_left = min(left, intervals[left_idx][0])
        new_right = max(right, intervals[right_idx - 1][1])
        return intervals[:left_idx] + [[new_left, new_right]] + intervals[right_idx:]


class TestInsertInterval:
    def test_example1(self):
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]
        assert Solution().insert(intervals, newInterval) == [[1, 5], [6, 9]]

    def test_example2(self):
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        expected = [[1, 2], [3, 10], [12, 16]]
        assert Solution().insert(intervals, newInterval) == expected
