# Title: Ransom Note
# URL: https://leetcode.com/problems/ransom-note/
# Difficulty: Easy


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        for char in magazine:
            magazine_dict[char] = magazine_dict.get(char, 0) + 1
        print(magazine_dict)

        for char in ransomNote:
            if char in magazine_dict:
                magazine_dict[char] -= 1
                if magazine_dict[char] < 0:
                    return False
            else:
                return False
        return True


class TestCanConstruct:
    def test_example1(self):
        ransomNote = "a"
        magazine = "aa"
        assert not Solution().canConstruct(ransomNote, magazine)

    def test_example2(self):
        ransomNote = "aa"
        magazine = "ab"
        assert not Solution().canConstruct(ransomNote, magazine)

    def test_example3(self):
        ransomNote = "aa"
        magazine = "aab"
        assert Solution().canConstruct(ransomNote, magazine)
