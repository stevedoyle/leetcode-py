# Title: 452. Minimum Number of Arrows to Burst Balloons
# URL: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# Difficulty: Medium

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]

        for start, point in points[1:]:
            if start > end:
                arrows += 1
                end = point

        return arrows


class TestFindMinArrowShots:
    def test_example1(self):
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]
        assert Solution().findMinArrowShots(points) == 2

    def test_example2(self):
        points = [[1, 2], [3, 4], [5, 6], [7, 8]]
        assert Solution().findMinArrowShots(points) == 4

    def test_example3(self):
        points = [[1, 2], [2, 3], [3, 4], [4, 5]]
        assert Solution().findMinArrowShots(points) == 2
