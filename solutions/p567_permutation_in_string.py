class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def to_key(s: str) -> str:
            return "".join(sorted(s))

        s1_key = to_key(s1)
        for i in range(len(s2) - len(s1) + 1):
            if to_key(s2[i : i + len(s1)]) == s1_key:
                return True
        return False


class TestCheckInclusion:
    def test_example1(self):
        s1 = "ab"
        s2 = "eidbaooo"
        expected = True
        s = Solution()
        result = s.checkInclusion(s1, s2)
        assert result == expected

    def test_example2(self):
        s1 = "ab"
        s2 = "eidboaoo"
        expected = False
        s = Solution()
        result = s.checkInclusion(s1, s2)
        assert result == expected

    def test_example3(self):
        s1 = "abc"
        s2 = "ccccbbbbaaaa"
        expected = False
        s = Solution()
        result = s.checkInclusion(s1, s2)
        assert result == expected
