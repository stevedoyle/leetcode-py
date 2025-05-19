from typing import List
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        result = 0
        curr = 0

        for num in nums:
            curr += num
            result += counts[curr - goal]
            counts[curr] += 1

        return result


class TestNumSubarraysWithSum:
    def test_example1(self):
        nums = [1, 0, 1, 0, 1]
        goal = 2
        expected = 4
        s = Solution()
        result = s.numSubarraysWithSum(nums, goal)
        assert result == expected

    def test_example2(self):
        nums = [0, 0, 0, 0, 0]
        goal = 0
        expected = 15
        s = Solution()
        result = s.numSubarraysWithSum(nums, goal)
        assert result == expected
