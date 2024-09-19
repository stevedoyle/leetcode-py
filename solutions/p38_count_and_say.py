# Link: https://leetcode.com/problems/count-and-say/
# Difficulty: Medium


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.say(self.countAndSay(n - 1))

    def say(self, s: str) -> str:
        i = 0
        result = ""
        while i < len(s):
            # Count the number of consecutive characters
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            # Write the count and the character
            result += str(count) + s[i]
            i += 1
        return result


class TestCountAndSay:
    def test_example1(self):
        n = 1
        expected = "1"
        assert Solution().countAndSay(n) == expected

    def test_example2(self):
        n = 4
        expected = "1211"
        assert Solution().countAndSay(n) == expected
