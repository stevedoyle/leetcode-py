class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for char in s:
            if char in seen:
                return char
            seen.add(char)
        return ""


class TestRepeatedCharacter:
    def test_example1(self):
        s = "abccbaacz"
        expected = "c"
        sol = Solution()
        result = sol.repeatedCharacter(s)
        assert result == expected

    def test_example2(self):
        s = "abcdd"
        expected = "d"
        sol = Solution()
        result = sol.repeatedCharacter(s)
        assert result == expected

    def test_example3(self):
        s = "aabbcc"
        expected = "a"
        sol = Solution()
        result = sol.repeatedCharacter(s)
        assert result == expected

    def test_example4(self):
        s = "xyz"
        expected = ""
        sol = Solution()
        result = sol.repeatedCharacter(s)
        assert result == expected
