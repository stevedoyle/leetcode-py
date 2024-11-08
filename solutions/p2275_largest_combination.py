# Title: 2275. Largest Combination With Bitwise AND Greater Than Zero
# URL: https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
# Difficulty: Medium

from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_count = [0] * 32
        for i in range(32):
            for candidate in candidates:
                if candidate & (1 << i):
                    bit_count[i] += 1
        return max(bit_count)


class TestLargestCombination:
    def test_example1(self):
        candidates = [16, 17, 71, 62, 12, 24, 14]
        assert Solution().largestCombination(candidates) == 4

    def test_example2(self):
        candidates = [8, 8]
        assert Solution().largestCombination(candidates) == 2
