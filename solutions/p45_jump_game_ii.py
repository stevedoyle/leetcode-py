from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_reachable = 0
        jumps = 0
        end = 0
        for i in range(n - 1):
            max_reachable = max(max_reachable, i + nums[i])
            if i == end:
                jumps += 1
                end = max_reachable
        return jumps


class TestJump:
    def test_example1(self):
        nums = [2, 3, 1, 1, 4]
        assert Solution().jump(nums) == 2

    def test_example2(self):
        nums = [2, 3, 0, 1, 4]
        assert Solution().jump(nums) == 2
