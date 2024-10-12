# Title: Divide Intervals into Minimum Number of Groups
# URL: https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/
# Difficulty: Medium

from typing import List
from collections import defaultdict


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        point_to_count = defaultdict(int)

        # Mark the starting and endpoing points in the dictionary
        for interval in intervals:
            point_to_count[interval[0]] += 1  # Start of an interval
            point_to_count[interval[1] + 1] -= 1  # End of an interval

        concurrent_intervals = 0
        max_concurrent_intervals = 0

        for point in sorted(point_to_count.keys()):
            concurrent_intervals += point_to_count[point]
            max_concurrent_intervals = max(
                max_concurrent_intervals, concurrent_intervals
            )

        return max_concurrent_intervals

    def minGroups2(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        groups = []
        for interval in intervals:
            for group in groups:
                if group[-1][1] < interval[0]:
                    group.append(interval)
                    break
            else:
                groups.append([interval])
        return len(groups)


class TestMinGroups:
    def test_example1(self):
        intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
        assert Solution().minGroups(intervals) == 3
        assert Solution().minGroups2(intervals) == 3

    def test_example2(self):
        intervals = [[1, 3], [5, 6], [8, 10], [11, 13]]
        assert Solution().minGroups(intervals) == 1
        assert Solution().minGroups2(intervals) == 1
