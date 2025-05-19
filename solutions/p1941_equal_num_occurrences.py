from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1


class TestAreOccurrencesEqual:
    def test_example1(self):
        s = "abacbc"
        expected = True
        sol = Solution()
        result = sol.areOccurrencesEqual(s)
        assert result == expected

    def test_example2(self):
        s = "aaabb"
        expected = False
        sol = Solution()
        result = sol.areOccurrencesEqual(s)
        assert result == expected

    def test_example3(self):
        s = "aabbcc"
        expected = True
        sol = Solution()
        result = sol.areOccurrencesEqual(s)
        assert result == expected
