from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        result = []

        for i, num in enumerate(nums):
            # Remove elements not in the window
            if window and window[0] < i - k + 1:
                window.popleft()

            # Remove smaller elements in k range as they are useless
            while window and nums[window[-1]] < num:
                window.pop()
            window.append(i)
            # Append the maximum for the current window
            if i >= k - 1:
                result.append(nums[window[0]])
        return result


class TestMaxSlidingWindow:
    def test_example1(self):
        assert Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [
            3,
            3,
            5,
            5,
            6,
            7,
        ]

    def test_example2(self):
        assert Solution().maxSlidingWindow([1], 1) == [1]

    def test_example3(self):
        assert Solution().maxSlidingWindow([1, -1], 1) == [1, -1]
