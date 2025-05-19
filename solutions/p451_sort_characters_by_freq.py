from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        return "".join(char * count for char, count in sorted_chars)


class TestFrequencySort:
    def test_example1(self):
        s = "tree"
        expected = ["eert", "eetr"]
        sol = Solution()
        result = sol.frequencySort(s)
        assert result in expected

    def test_example2(self):
        s = "cccaaa"
        expected = ["cccaaa", "aaaccc"]
        sol = Solution()
        result = sol.frequencySort(s)
        assert result in expected

    def test_example3(self):
        s = "Aabb"
        expected = ["bbAa", "Aabb"]
        sol = Solution()
        result = sol.frequencySort(s)
        assert result in expected
