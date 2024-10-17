# Title: Find the Index of the First Occurrence in a String
# URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
# Difficulty: Easy


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                if haystack[i : i + len(needle)] == needle:
                    return i

        return -1


class TestStrStr:
    def test_example1(self):
        haystack = "sadbutsad"
        needle = "sad"
        assert Solution().strStr(haystack, needle) == 0

    def test_example2(self):
        haystack = "leetcode"
        needle = "leeto"
        assert Solution().strStr(haystack, needle) == -1

    def test_example3(self):
        haystack = "hello"
        needle = "ll"
        assert Solution().strStr(haystack, needle) == 2
