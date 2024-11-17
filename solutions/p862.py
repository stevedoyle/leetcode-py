# Title: Shortest Subarray with Sum at Least K
# URL: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
# Difficulty: Hard

from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        ans = n + 1
        deque = []
        for i in range(n + 1):
            while deque and prefix_sum[i] - prefix_sum[deque[0]] >= k:
                ans = min(ans, i - deque.pop(0))
            while deque and prefix_sum[i] <= prefix_sum[deque[-1]]:
                deque.pop()
            deque.append(i)

        return ans if ans != n + 1 else -1


class TestShortestSubarray:
    def test_example1(self):
        nums = [1]
        k = 1
        expected = 1
        assert Solution().shortestSubarray(nums, k) == expected

    def test_example2(self):
        nums = [1, 2]
        k = 4
        expected = -1
        assert Solution().shortestSubarray(nums, k) == expected

    def test_example3(self):
        nums = [2, -1, 2]
        k = 3
        expected = 3
        assert Solution().shortestSubarray(nums, k) == expected
