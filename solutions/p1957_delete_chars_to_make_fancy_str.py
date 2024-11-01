# Title: Delete Characters to Make Fancy String
# URL: https://leetcode.com/problems/delete-characters-to-make-fancy-string/
# Difficulty: Easy


class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        fancy = [s[:2]]
        for i in range(2, len(s)):
            if s[i] == s[i - 1] == s[i - 2]:
                continue
            fancy.append(s[i])

        return "".join(fancy)


class TestMakeFancyString:
    def test_example1(self):
        s = "leeetcode"
        assert Solution().makeFancyString(s) == "leetcode"

    def test_example2(self):
        s = "aaabaaaa"
        assert Solution().makeFancyString(s) == "aabaa"

    def test_example3(self):
        s = "aab"
        assert Solution().makeFancyString(s) == "aab"
