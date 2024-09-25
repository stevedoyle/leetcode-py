# Title: Sum of Prefix Scores of Strings
# URL: https://leetcode.com/problems/sum-of-prefix-scores-of-strings/
# Difficulty: Hard

from typing import List


class trie_node:
    def __init__(self):
        self.next = [None] * 26
        self.cnt = 0


class Solution:
    def __init__(self):
        # Initialize the root node of the trie.
        self.root = trie_node()

    # Insert function for the word.
    def insert(self, word):
        node = self.root
        for c in word:
            idx = ord(c) - ord("a")
            # If new prefix, create a new trie node.
            if node.next[idx] is None:
                node.next[idx] = trie_node()
            # Increment the count of the current prefix.
            node.next[idx].cnt += 1
            node = node.next[idx]

    # Calculate the prefix count using this function.
    def count(self, s):
        node = self.root
        ans = 0
        # The ans would store the total sum of counts.
        for c in s:
            idx = ord(c) - ord("a")
            ans += node.next[idx].cnt
            node = node.next[idx]
        return ans

    def sumPrefixScores(self, words):
        # Insert words in trie.
        for word in words:
            self.insert(word)
        # Calculate the prefix count for each word.
        scores = [self.count(word) for word in words]
        return scores

    def sumPrefixScoresSlow(self, words: List[str]) -> List[int]:
        scores = []
        dp = {}
        for word in words:
            prefixes = self.getPrefixes(word)
            score = 0
            for prefix in prefixes:
                if prefix in dp:
                    score += dp[prefix]
                else:
                    dp[prefix] = self.getPrefixScores(prefix, words)
                    score += dp[prefix]
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

    def test_example1_slow(self):
        words = ["abc", "ab", "bc", "b"]
        assert Solution().sumPrefixScoresSlow(words) == [5, 4, 3, 2]

    def test_example2_slow(self):
        words = ["abcd"]
        assert Solution().sumPrefixScoresSlow(words) == [4]

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
