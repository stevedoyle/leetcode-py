# Title: Jump Game
# URL: https://leetcode.com/problems/jump-game/
# Difficulty: Medium

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reachable = 0
        for i in range(n):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + nums[i])
        return True


class TestCanJump:
    def test_example1(self):
        nums = [2, 3, 1, 1, 4]
        assert Solution().canJump(nums)

    def test_example2(self):
        nums = [3, 2, 1, 0, 4]
        assert not Solution().canJump(nums)
