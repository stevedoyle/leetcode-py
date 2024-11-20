# Title: Take K of Each Character From Left and Right
# URL: https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/
# Difficulty: Medium


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        count = [0] * 3

        for c in s:
            count[ord(c) - ord("a")] += 1

        for i in range(3):
            if count[i] < k:
                return -1

        window = [0] * 3
        left, max_window = 0, 0

        for right in range(n):
            window[ord(s[right]) - ord("a")] += 1

            while left <= right and (
                count[0] - window[0] < k
                or count[1] - window[1] < k
                or count[2] - window[2] < k
            ):
                window[ord(s[left]) - ord("a")] -= 1
                left += 1

            max_window = max(max_window, right - left + 1)
        return n - max_window


class TestTakeCharacters:
    def test_example1(self):
        s = "aabaaaacaabc"
        k = 2
        expected = 8
        assert Solution().takeCharacters(s, k) == expected

    def test_example2(self):
        s = "a"
        k = 1
        expected = -1
        assert Solution().takeCharacters(s, k) == expected
