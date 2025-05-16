class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Given a string s, reverse the order of characters in each word within
        a sentence while still preserving whitespace and initial word order.
        """
        words = s.split()
        reversed_words = [word[::-1] for word in words]
        return " ".join(reversed_words)

    def reverseWord(self, s: str) -> str:
        """
        Given a string s, reverse the order of characters in the string.
        """
        letters = list(s)
        left, right = 0, len(letters) - 1
        while left < right:
            letters[left], letters[right] = letters[right], letters[left]
            left += 1
            right -= 1
        return "".join(letters)


class TestReverseWords:
    def test_example1(self):
        s = "Let's take LeetCode contest"
        expected = "s'teL ekat edoCteeL tsetnoc"
        solution = Solution()
        result = solution.reverseWords(s)
        assert result == expected

    def test_example2(self):
        s = "God Ding"
        expected = "doG gniD"
        solution = Solution()
        result = solution.reverseWords(s)
        assert result == expected
