# Title: Isomorphic Strings
# URL: https://leetcode.com/problems/isomorphic-strings/
# Difficulty: Easy


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_t = {}
        mapping_t_s = {}

        for s_char, t_char in zip(s, t):
            if (s_char not in mapping_s_t) and (t_char not in mapping_t_s):
                mapping_s_t[s_char] = t_char
                mapping_t_s[t_char] = s_char
            elif mapping_s_t.get(s_char) != t_char or mapping_t_s.get(t_char) != s_char:
                return False

        return True


class TestIsIsomorphic:
    def test_example1(self):
        s = "egg"
        t = "add"
        assert Solution().isIsomorphic(s, t)

    def test_example2(self):
        s = "foo"
        t = "bar"
        assert not Solution().isIsomorphic(s, t)

    def test_example3(self):
        s = "paper"
        t = "title"
        assert Solution().isIsomorphic(s, t)

    def test_example4(self):
        s = "badc"
        t = "baba"
        assert not Solution().isIsomorphic(s, t)
