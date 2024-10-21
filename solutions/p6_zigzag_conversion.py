# Title: ZigZag Conversion
# URL: https://leetcode.com/problems/zigzag-conversion/
# Difficulty: Medium


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows
        i = 0
        direction = 1
        for c in s:
            rows[i] += c
            i += direction
            if i == numRows - 1:
                direction = -1
            if i == 0:
                direction = 1
        print(rows)
        return "".join(rows)


class TestConvert:
    def test_example1(self):
        s = "PAYPALISHIRING"
        numRows = 3
        expected = "PAHNAPLSIIGYIR"
        assert Solution().convert(s, numRows) == expected

    def test_example2(self):
        s = "PAYPALISHIRING"
        numRows = 4
        expected = "PINALSIGYAHRPI"
        assert Solution().convert(s, numRows) == expected

    def test_example3(self):
        s = "A"
        numRows = 1
        expected = "A"
        assert Solution().convert(s, numRows) == expected
