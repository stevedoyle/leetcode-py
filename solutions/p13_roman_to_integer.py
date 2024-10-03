# Title: Roman to Integer
# URL: https://leetcode.com/problems/roman-to-integer/
# Difficulty: Easy


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev = 0
        for char in s:
            curr = roman_to_int[char]
            if prev < curr:
                result += curr - 2 * prev
            else:
                result += curr
            prev = curr
        return result


class TestRomanToInt:
    def test_example1(self):
        assert Solution().romanToInt("III") == 3

    def test_example2(self):
        assert Solution().romanToInt("IV") == 4

    def test_example3(self):
        assert Solution().romanToInt("IX") == 9
