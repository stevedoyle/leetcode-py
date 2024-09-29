# Title: Find the Lexicographically Smallest Valid Sequence
# Link: https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/
# Difficulty: Medium

from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word2)
        last = [-1] * n
        j = n - 1
        for i, ch in reversed(list(enumerate(word1))):
            if j >= 0 and ch == word2[j]:
                last[j] = i
                j -= 1
        j = cnt = 0
        ans = []
        for i, ch in enumerate(word1):
            if j < n:
                if ch == word2[j] or cnt == 0 and (j == n - 1 or i + 1 <= last[j + 1]):
                    if ch != word2[j]:
                        cnt = 1
                    ans.append(i)
                    j += 1
        return ans if j == n else []


class TestValidSequence:
    def test_example1(self):
        solution = Solution()
        word1 = "vbcca"
        word2 = "abc"
        expected = [0, 1, 2]
        assert solution.validSequence(word1, word2) == expected

    def test_example2(self):
        solution = Solution()
        word1 = "bacdc"
        word2 = "abc"
        expected = [1, 2, 4]
        assert solution.validSequence(word1, word2) == expected

    def test_example3(self):
        solution = Solution()
        word1 = "aaaaaa"
        word2 = "aaabc"
        expected = []
        assert solution.validSequence(word1, word2) == expected
