# Title: Merge Intervals
# URL: https://leetcode.com/problems/merge-intervals/
# Difficulty: Medium

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


class TestMerge:
    def test_example1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        assert Solution().merge(intervals) == expected

    def test_example2(self):
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        assert Solution().merge(intervals) == expected
