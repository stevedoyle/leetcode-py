# Title: 392. Is Subsequence
# URL: https://leetcode.com/problems/is-subsequence/
# Difficulty: Easy


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0

        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
                t_index += 1
            else:
                t_index += 1
        return s_index == len(s)


class TestIsSubsequence:
    def test_example1(self):
        s = "abc"
        t = "ahbgdc"
        assert Solution().isSubsequence(s, t)

    def test_example2(self):
        s = "axc"
        t = "ahbgdc"
        assert not Solution().isSubsequence(s, t)
