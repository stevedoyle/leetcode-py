# Title: Number of 1 Bits
# URL: https://leetcode.com/problems/number-of-1-bits/
# Difficulty: Easy


class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()


class TestHammingWeight:
    def test_example1(self):
        n = 11
        assert Solution().hammingWeight(n) == 3

    def test_example2(self):
        n = 128
        assert Solution().hammingWeight(n) == 1

    def test_example3(self):
        n = 2147483645
        assert Solution().hammingWeight(n) == 30
