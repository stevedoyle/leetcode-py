# Title: Split a String Into the Max Number of Unique Substrings
# URL: https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
# Difficulty: Medium


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, path):
            if start == len(s):
                return len(path)

            max_unique_substrings = 0
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in path:
                    max_unique_substrings = max(
                        max_unique_substrings, backtrack(end, path | {substring})
                    )

            return max_unique_substrings

        return backtrack(0, set())


class TestMaxUniqueSplit:
    def test_example1(self):
        s = "ababccc"
        expected = 5
        assert Solution().maxUniqueSplit(s) == expected

    def test_example2(self):
        s = "aba"
        expected = 2
        assert Solution().maxUniqueSplit(s) == expected

    def test_example3(self):
        s = "aa"
        expected = 1
        assert Solution().maxUniqueSplit(s) == expected
