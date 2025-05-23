from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = deque()
        decreasing = deque()
        left = 0
        max_length = 0

        for right in range(len(nums)):
            while increasing and nums[increasing[-1]] < nums[right]:
                increasing.pop()
            while decreasing and nums[decreasing[-1]] > nums[right]:
                decreasing.pop()

            increasing.append(right)
            decreasing.append(right)

            while nums[increasing[0]] - nums[decreasing[0]] > limit:
                left += 1
                if increasing[0] < left:
                    increasing.popleft()
                if decreasing[0] < left:
                    decreasing.popleft()

            max_length = max(max_length, right - left + 1)
        return max_length


class TestLongestSubarray:
    def test_example1(self):
        assert Solution().longestSubarray([8, 2, 4, 7], 4) == 2

    def test_example2(self):
        assert Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5) == 4

    def test_example3(self):
        assert Solution().longestSubarray([4, 2, 2, 2, 4, 4], 0) == 3
