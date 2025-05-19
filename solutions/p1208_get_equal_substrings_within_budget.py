# LeetCode Problem 1208
# Given two strings s and t, return the maximum length of a substring that
# can be obtained by replacing at most maxCost characters in s with characters from t.
# The cost of replacing a character is the absolute difference between the ASCII values of the characters.
# The substring must be contiguous and can be of any length.


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        if len(s) != len(t):
            return 0
        left = right = 0
        max_length = 0
        current_cost = 0

        for right in range(len(s)):
            current_cost += abs(ord(s[right]) - ord(t[right]))
            while current_cost > maxCost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length


class TestEqualSubstring:
    def test_example1(self):
        s = "abcd"
        t = "bcdf"
        maxCost = 3
        expected = 3
        sol = Solution()
        result = sol.equalSubstring(s, t, maxCost)
        assert result == expected

    def test_example2(self):
        s = "abcd"
        t = "cdef"
        maxCost = 3
        expected = 1
        sol = Solution()
        result = sol.equalSubstring(s, t, maxCost)
        assert result == expected

    def test_example3(self):
        s = "abcd"
        t = "acde"
        maxCost = 0
        expected = 1
        sol = Solution()
        result = sol.equalSubstring(s, t, maxCost)
        assert result == expected
