# Title: Shortest Subarray with OR >= k II
# URL: https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/
# Difficulty: Medium

from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_length = float("inf")
        window_start = window_end = 0
        bit_counts = [0] * 32  # Track the count of 1s at each bit position

        while window_end < len(nums):
            self._update_bit_counts(bit_counts, nums[window_end], 1)

            while (
                window_start <= window_end
                and self._convert_bits_to_num(bit_counts) >= k
            ):
                min_length = min(min_length, window_end - window_start + 1)
                self._update_bit_counts(bit_counts, nums[window_start], -1)
                window_start += 1

            window_end += 1

        return -1 if min_length == float("inf") else min_length

    def _update_bit_counts(self, bit_counts: List[int], num: int, delta: int) -> None:
        for i in range(32):
            if num & (1 << i):
                bit_counts[i] += delta

    def _convert_bits_to_num(self, bit_counts: List[int]) -> int:
        result = 0
        for i in range(32):
            if bit_counts[i] > 0:
                result |= 1 << i

        return result


class TestMinimumSubarrayLength:
    def test_example1(self):
        assert Solution().minimumSubarrayLength([1, 2, 3], 2) == 1

    def test_example2(self):
        assert Solution().minimumSubarrayLength([2, 1, 8], 10) == 3

    def test_example3(self):
        assert Solution().minimumSubarrayLength([1, 2], 1) == 1
