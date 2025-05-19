from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        current_altitude = 0
        for g in gain:
            current_altitude += g
            max_altitude = max(max_altitude, current_altitude)
        return max_altitude


class TestLargestAltitude:
    def test_example1(self):
        gain = [-5, 1, 5, 0, -7]
        expected = 1
        s = Solution()
        result = s.largestAltitude(gain)
        assert result == expected

    def test_example2(self):
        gain = [-4, -3, -2, -1, 4, 3, 2]
        expected = 0
        s = Solution()
        result = s.largestAltitude(gain)
        assert result == expected

    def test_example3(self):
        gain = [1, 2, 3]
        expected = 6
        s = Solution()
        result = s.largestAltitude(gain)
        assert result == expected
