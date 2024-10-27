# Title: Reverse Bits
# URL: https://leetcode.com/problems/reverse-bits/
# Difficulty: Easy


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result


class TestReverseBits:
    def test_example1(self):
        n = 43261596
        expected = 964176192
        assert Solution().reverseBits(n) == expected

    def test_example2(self):
        n = 4294967293
        expected = 3221225471
        assert Solution().reverseBits(n) == expected
