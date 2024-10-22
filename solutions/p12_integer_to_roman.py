# Title: Integer to Roman
# URL: https://leetcode.com/problems/integer-to-roman/
# Difficulty: Medium


class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        roman = ""
        for val, symbol in values:
            while num >= val:
                roman += symbol
                num -= val
        return roman


class TestIntToRoman:
    def test_example1(self):
        num = 3749
        expected = "MMMDCCXLIX"
        assert Solution().intToRoman(num) == expected

    def test_example2(self):
        num = 58
        expected = "LVIII"
        assert Solution().intToRoman(num) == expected

    def test_example3(self):
        num = 1994
        expected = "MCMXCIV"
        assert Solution().intToRoman(num) == expected
