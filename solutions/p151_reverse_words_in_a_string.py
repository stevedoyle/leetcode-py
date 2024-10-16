# Title: 151. Reverse Words in a String
# URL: https://leetcode.com/problems/reverse-words-in-a-string/
# Difficulty: Medium


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


class TestReverseWords:
    def test_example1(self):
        s = "the sky is blue"
        assert Solution().reverseWords(s) == "blue is sky the"

    def test_example2(self):
        s = "a good  example"
        assert Solution().reverseWords(s) == "example good a"
