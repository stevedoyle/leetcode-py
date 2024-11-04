# Title: 3163. String Compression III
# URL: https://leetcode.com/problems/string-compression-iii/
# Difficulty: Medium


class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""
        comp = ""
        current_c = word[0]
        count = 1
        for c in word[1:]:
            if c == current_c:
                count += 1
                if count == 9:
                    comp += "9" + current_c
                    count = 0
            else:
                if count > 0:
                    comp += str(count) + current_c
                current_c = c
                count = 1

        if count > 0:
            comp += str(count) + current_c
        return comp


class TestCompressedString:
    def test_example1(self):
        word = "abcde"
        excpected = "1a1b1c1d1e"
        assert Solution().compressedString(word) == excpected

    def test_example2(self):
        word = "aaaaaaaaaaaaaabb"
        excpected = "9a5a2b"
        assert Solution().compressedString(word) == excpected

    def test_example3(self):
        word = "aabbaa"
        excpected = "2a2b2a"
        assert Solution().compressedString(word) == excpected

    def test_example4(self):
        word = "cccccccccc"
        expected = "9c1c"
        assert Solution().compressedString(word) == expected
