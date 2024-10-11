# Title: Gas Station
# URL: https://leetcode.com/problems/gas-station/
# Difficulty: Medium

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_tank = 0
        curr_tank = 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                starting_station = i + 1
                curr_tank = 0

        return starting_station if total_tank >= 0 else -1


class TestCanCompleteCircuit:
    def test_example1(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        expected = 3
        s = Solution()
        result = s.canCompleteCircuit(gas, cost)
        assert result == expected

    def test_example2(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        expected = -1
        s = Solution()
        result = s.canCompleteCircuit(gas, cost)
        assert result == expected
