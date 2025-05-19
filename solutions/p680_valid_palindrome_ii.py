# 680: Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/
# Difficulty: Easy


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return check_palindrome(left + 1, right) or check_palindrome(
                    left, right - 1
                )
            left += 1
            right -= 1
        return True


class TestValidPalindrome:
    def test_example1(self):
        s = "aba"
        expected = True
        sol = Solution()
        result = sol.validPalindrome(s)
        assert result == expected

    def test_example2(self):
        s = "abca"
        expected = True
        sol = Solution()
        result = sol.validPalindrome(s)
        assert result == expected

    def test_example3(self):
        s = "abc"
        expected = False
        sol = Solution()
        result = sol.validPalindrome(s)
        assert result == expected
