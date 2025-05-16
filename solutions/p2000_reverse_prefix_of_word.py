class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        Given a string word and a character ch, reverse the substring starting from the beginning of word up to and including the first occurrence of ch.
        If the character ch does not exist in word, do nothing.
        Return the resulting string.
        """
        index = word.find(ch)
        if index == -1:
            return word
        # Reverse the substring from the beginning to the index of ch
        # and concatenate it with the rest of the string
        left = 0
        right = index
        letters = list(word)  # Convert string to list for mutability
        while left < right:
            letters[left], letters[right] = letters[right], letters[left]
            left += 1
            right -= 1
        return "".join(letters)


class TestReversePrefix:
    def test_example1(self):
        word = "abcdefd"
        ch = "d"
        expected = "dcbaefd"
        s = Solution()
        result = s.reversePrefix(word, ch)
        assert result == expected

    def test_example2(self):
        word = "xyxzxe"
        ch = "z"
        expected = "zxyxxe"
        s = Solution()
        result = s.reversePrefix(word, ch)
        assert result == expected

    def test_example3(self):
        word = "abcd"
        ch = "z"
        expected = "abcd"
        s = Solution()
        result = s.reversePrefix(word, ch)
        assert result == expected
