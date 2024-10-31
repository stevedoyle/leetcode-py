# Title: Minimum Total Distance Traveled
# URL: https://leetcode.com/problems/minimum-total-distance-traveled/
# Difficulty: Hard

from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])
        factory_positions = []
        for f in factory:
            factory_positions.extend([f[0]] * f[1])
        robot_count = len(robot)
        factory_count = len(factory_positions)

        dp = [[None] * (factory_count + 1) for _ in range(robot_count + 1)]

        def min_distance(robot_idx: int, factory_idx: int) -> int:
            if dp[robot_idx][factory_idx] is not None:
                return dp[robot_idx][factory_idx]
            if robot_idx == robot_count:
                dp[robot_idx][factory_idx] = 0
                return 0
            if factory_idx == factory_count:
                dp[robot_idx][factory_idx] = int(1e12)
                return int(1e12)

            assign = abs(
                robot[robot_idx] - factory_positions[factory_idx]
            ) + min_distance(robot_idx + 1, factory_idx + 1)
            skip = min_distance(robot_idx, factory_idx + 1)

            dp[robot_idx][factory_idx] = min(assign, skip)
            return dp[robot_idx][factory_idx]

        return min_distance(0, 0)


class TestMinimumTotalDistance:
    def test_example1(self):
        robot = [0, 4, 6]
        factory = [[2, 2], [6, 2]]
        assert Solution().minimumTotalDistance(robot, factory) == 4

    def test_example2(self):
        robot = [1, -1]
        factory = [[-2, 1], [2, 1]]
        assert Solution().minimumTotalDistance(robot, factory) == 2
