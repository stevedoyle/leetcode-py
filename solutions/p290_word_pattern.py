# Title: 290. Word Pattern
# URL: https://leetcode.com/problems/word-pattern/
# Difficulty: Easy

from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        mapping = defaultdict(str)
        seen = set()

        for letter, word in zip(pattern, words):
            if letter in mapping:
                if mapping[letter] != word:
                    return False
            elif word in seen:
                return False
            else:
                mapping[letter] = word
                seen.add(word)

        return True


class TestWordPattern:
    def test_example1(self):
        pattern = "abba"
        s = "dog cat cat dog"
        assert Solution().wordPattern(pattern, s)

    def test_example2(self):
        pattern = "abba"
        s = "dog cat cat fish"
        assert not Solution().wordPattern(pattern, s)

    def test_example3(self):
        pattern = "aaaa"
        s = "dog cat cat dog"
        assert not Solution().wordPattern(pattern, s)

    def test_example4(self):
        pattern = "abba"
        s = "dog dog dog dog"
        assert not Solution().wordPattern(pattern, s)

    def test_example5(self):
        pattern = "abc"
        s = "dog cat dog"
        assert not Solution().wordPattern(pattern, s)
