# Title: Valid Anagram
# URL: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class TestIsAnagram:
    def test_example1(self):
        s = "anagram"
        t = "nagaram"
        expected = True
        assert Solution().isAnagram(s, t) == expected

    def test_example2(self):
        s = "rat"
        t = "car"
        expected = False
        assert Solution().isAnagram(s, t) == expected
