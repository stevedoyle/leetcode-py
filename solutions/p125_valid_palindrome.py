# Title: Valid Palindrome
# URL: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        s = "".join(filter(str.isalnum, s)).lower()
        return s == s[::-1]


class TestIsPalindrome:
    def test_examples1(self):
        s = "A man, a plan, a canal: Panama"
        assert Solution().isPalindrome(s)

    def test_examples2(self):
        s = "race a car"
        assert not Solution().isPalindrome(s)

    def test_examples3(self):
        s = " "
        assert Solution().isPalindrome(s)
