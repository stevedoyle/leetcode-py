# Title: Longest Common Prefix
# URL: https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return prefix
        return prefix


class TestLongestCommonPrefix:
    def test_example1(self):
        assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"

    def test_example2(self):
        assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""

    def test_example3(self):
        assert Solution().longestCommonPrefix(["a"]) == "a"
