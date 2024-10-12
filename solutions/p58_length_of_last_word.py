# Title: Length of Last Word
# URL: https://leetcode.com/problems/length-of-last-word/
# Difficulty: Easy


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])


class TestLengthOfLastWord:
    def test_example1(self):
        assert Solution().lengthOfLastWord("Hello World") == 5

    def test_example2(self):
        assert Solution().lengthOfLastWord("   fly me   to   the moon ") == 4

    def test_example3(self):
        assert Solution().lengthOfLastWord("luffy is still joyboy") == 6
