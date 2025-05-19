# Title: 1456. Maximum Number of Vowels in a Substring of Given Length
# URL: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Difficulty: Medium


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = right = 0
        max_vowels = 0
        vowels = set("aeiou")
        current_vowels = 0
        while right < len(s):
            if s[right] in vowels:
                current_vowels += 1
            if right - left + 1 > k:
                if s[left] in vowels:
                    current_vowels -= 1
                left += 1
            max_vowels = max(max_vowels, current_vowels)
            right += 1
        return max_vowels


class TestMaxVowels:
    def test_example1(self):
        s = "abciiidef"
        k = 3
        expected = 3
        sol = Solution()
        result = sol.maxVowels(s, k)
        assert result == expected

    def test_example2(self):
        s = "aeiou"
        k = 2
        expected = 2
        sol = Solution()
        result = sol.maxVowels(s, k)
        assert result == expected

    def test_example3(self):
        s = "leetcode"
        k = 3
        expected = 2
        sol = Solution()
        result = sol.maxVowels(s, k)
        assert result == expected
