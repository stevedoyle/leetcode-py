# Title: Minimum Window Substring
# URL: https://leetcode.com/problems/minimum-window-substring/
# Difficulty: Hard

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        required = len(t_count)
        formed = 0
        window_count = {}
        left, right = 0, 0
        # ans = (window length, left, right)
        ans = float("inf"), None, None

        while right < len(s):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            while left <= right and formed == required:
                char = s[left]
                if right - left + 1 < ans[0]:
                    ans = right - left + 1, left, right
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                left += 1
            right += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


class TestMinWindow:
    def test_example1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        expected = "BANC"
        assert Solution().minWindow(s, t) == expected

    def test_example2(self):
        s = "a"
        t = "a"
        expected = "a"
        assert Solution().minWindow(s, t) == expected

    def test_example3(self):
        s = "a"
        t = "aa"
        expected = ""
        assert Solution().minWindow(s, t) == expected

    def test_example4(self):
        s = "a"
        t = "b"
        expected = ""
        assert Solution().minWindow(s, t) == expected
