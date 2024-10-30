# Title: Meeting Rooms II
# URL: https://leetcode.com/problems/meeting-rooms-ii/
# Difficulty: Medium

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        used_rooms = 0
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])

        start_idx = end_idx = 0

        while start_idx < len(intervals):
            if start_times[start_idx] >= end_times[end_idx]:
                end_idx += 1
            elif start_times[start_idx] < end_times[end_idx]:
                used_rooms += 1
            start_idx += 1

        return used_rooms


class TestMinMeetingRooms:
    def test_example1(self):
        intervals = [[0, 30], [5, 10], [15, 20]]
        expected = 2
        assert Solution().minMeetingRooms(intervals) == expected

    def test_example2(self):
        intervals = [[7, 10], [2, 4]]
        expected = 1
        assert Solution().minMeetingRooms(intervals) == expected

    def test_example3(self):
        intervals = [[2, 7]]
        expected = 1
        assert Solution().minMeetingRooms(intervals) == expected

    def test_example4(self):
        intervals = [[1, 5], [8, 9], [8, 9]]
        expected = 2
        assert Solution().minMeetingRooms(intervals) == expected
