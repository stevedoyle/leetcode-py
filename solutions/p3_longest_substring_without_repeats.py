# Title: Longest Substring Without Repeating Characters
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = 0
        seen = {}
        for i, c in enumerate(s):
            if c in seen and seen[c] >= start:
                start = seen[c] + 1
            seen[c] = i
            max_len = max(max_len, i - start + 1)
        return max_len


class TestLengthOfLongestSubstring:
    def test_example1(self):
        s = "abcabcbb"
        assert Solution().lengthOfLongestSubstring(s) == 3

    def test_example2(self):
        s = "bbbbb"
        assert Solution().lengthOfLongestSubstring(s) == 1

    def test_example3(self):
        s = "pwwkew"
        assert Solution().lengthOfLongestSubstring(s) == 3
