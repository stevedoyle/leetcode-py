# Title: Sum of Prefix Scores of Strings
# URL: https://leetcode.com/problems/sum-of-prefix-scores-of-strings/
# Difficulty: Hard

from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        scores = []
        for word in words:
            prefixes = self.getPrefixes(word)
            score = 0
            for prefix in prefixes:
                score += self.getPrefixScores(prefix, words)
            scores.append(score)
        return scores

    def getPrefixScores(self, prefix: str, words: List[str]) -> int:
        score = 0
        for word in words:
            if word.startswith(prefix):
                score += 1
        return score

    def getPrefixes(self, word: str) -> List[str]:
        prefixes = [word[:i] for i in range(1, len(word) + 1)]
        return prefixes


class TestSumPrefixSocres:
    def test_example1(self):
        words = ["abc", "ab", "bc", "b"]
        assert Solution().sumPrefixScores(words) == [5, 4, 3, 2]

    def test_example2(self):
        words = ["abcd"]
        assert Solution().sumPrefixScores(words) == [4]

    def test_prefixes(self):
        word = "abc"
        assert Solution().getPrefixes(word) == ["a", "ab", "abc"]

        word = "abcd"
        assert Solution().getPrefixes(word) == ["a", "ab", "abc", "abcd"]

        word = "ab"
        assert Solution().getPrefixes(word) == ["a", "ab"]

        word = "b"
        assert Solution().getPrefixes(word) == ["b"]

    def test_getPrefixScores(self):
        prefix = "a"
        words = ["abc", "ab", "bc", "b"]
        assert Solution().getPrefixScores(prefix, words) == 2

        prefix = "ab"
        words = ["abc", "ab", "bc", "b"]
        assert Solution().getPrefixScores(prefix, words) == 2

        prefix = "abc"
        words = ["abc", "ab", "bc", "b"]
        assert Solution().getPrefixScores(prefix, words) == 1

        prefix = "b"
        words = ["abc", "ab", "bc", "b"]
        assert Solution().getPrefixScores(prefix, words) == 2

        prefix = "bc"
        words = ["abc", "ab", "bc", "b"]
        assert Solution().getPrefixScores(prefix, words) == 1
