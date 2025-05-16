class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """
        Given a string s, reverse the string according to the following rules:
        1. All characters that are not English letters remain in the same position.
        2. All English letters (lowercase or uppercase) should be reversed.
        Return s after reversing it.
        """
        letters = list(s)
        left, right = 0, len(letters) - 1
        while left < right:
            if letters[left].isalpha() and letters[right].isalpha():
                letters[left], letters[right] = letters[right], letters[left]
                left += 1
                right -= 1
            elif not letters[left].isalpha():
                left += 1
            else:
                right -= 1
        return "".join(letters)


class TestReverseOnlyLetters:
    def test_example1(self):
        s = "ab-cd"
        expected = "dc-ba"
        solution = Solution()
        result = solution.reverseOnlyLetters(s)
        assert result == expected

    def test_example2(self):
        s = "a-bC-dEf-ghIj"
        expected = "j-Ih-gfE-dCba"
        solution = Solution()
        result = solution.reverseOnlyLetters(s)
        assert result == expected

    def test_example3(self):
        s = "Test1ng-Leet=code-Q!"
        expected = "Qedo1ct-eeLg=ntse-T!"
        solution = Solution()
        result = solution.reverseOnlyLetters(s)
        assert result == expected
