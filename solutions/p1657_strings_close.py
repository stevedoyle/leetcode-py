# 1675. Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/
# Difficulty: Medium

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        # Count the frequency of each character in both words
        count1 = Counter(word1)
        count2 = Counter(word2)

        # Check if both words have the same set of characters
        if set(count1.keys()) != set(count2.keys()):
            return False

        # Check if the frequency counts can be rearranged to match
        return sorted(count1.values()) == sorted(count2.values())


class TestCloseStrings:
    def test_example1(self):
        word1 = "abc"
        word2 = "bca"
        expected = True
        s = Solution()
        result = s.closeStrings(word1, word2)
        assert result == expected

    def test_example2(self):
        word1 = "a"
        word2 = "aa"
        expected = False
        s = Solution()
        result = s.closeStrings(word1, word2)
        assert result == expected

    def test_example3(self):
        word1 = "cabbba"
        word2 = "abbccc"
        expected = True
        s = Solution()
        result = s.closeStrings(word1, word2)
        assert result == expected
