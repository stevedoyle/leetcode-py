# Title: 1942. The Number of the Smallest Unoccupied Chair
# URL: https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/
# Difficulty: Medium

from typing import List
import heapq


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []
        for i in range(len(times)):
            events.append((times[i][0], i))  # Arrival event
            events.append((times[i][1], -i))  # Leave event

        events.sort()

        available = list(range(len(times)))
        occupied = []

        for time, friend in events:
            while occupied and occupied[0][0] <= time:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(available, chair)

            if friend >= 0:
                chair = heapq.heappop(available)
                if friend == targetFriend:
                    return chair
                heapq.heappush(occupied, (times[friend][1], chair))

        return -1


class TestSmallestChair:
    def test_example1(self):
        times = [[1, 4], [2, 3], [4, 6]]
        targetFriend = 1
        expected = 1
        assert Solution().smallestChair(times, targetFriend) == expected

    def test_example2(self):
        times = [[3, 10], [1, 5], [2, 6]]
        targetFriend = 0
        expected = 2
        assert Solution().smallestChair(times, targetFriend) == expected

    def test_example3(self):
        times = [
            [33889, 98676],
            [80071, 89737],
            [44118, 52565],
            [52992, 84310],
            [78492, 88209],
            [21695, 67063],
            [84622, 95452],
            [98048, 98856],
            [98411, 99433],
            [55333, 56548],
            [65375, 88566],
            [55011, 62821],
            [48548, 48656],
            [87396, 94825],
            [55273, 81868],
            [75629, 91467],
        ]
        targetFriend = 6
        expected = 2
        assert Solution().smallestChair(times, targetFriend) == expected
