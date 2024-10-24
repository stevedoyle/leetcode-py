# Title: Add Binary
# URL: https://leetcode.com/problems/add-binary/
# Difficulty: Easy


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinaryv2(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]


class TestAddBinary:
    def test_example1(self):
        a = "11"
        b = "1"
        assert Solution().addBinary(a, b) == "100"
        assert Solution().addBinaryv2(a, b) == "100"

    def test_example2(self):
        a = "1010"
        b = "1011"
        assert Solution().addBinaryv2(a, b) == "10101"
