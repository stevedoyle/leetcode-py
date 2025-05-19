from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if len(nums) != 3:
            return "none"

        a, b, c = sorted(nums)
        if a + b <= c:
            return "none"
        elif a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"


class TestTriangleType:
    def test_example1(self):
        nums = [2, 2, 3]
        expected = "isosceles"
        s = Solution()
        result = s.triangleType(nums)
        assert result == expected

    def test_example2(self):
        nums = [3, 4, 5]
        expected = "scalene"
        s = Solution()
        result = s.triangleType(nums)
        assert result == expected

    def test_example3(self):
        nums = [1, 1, 1]
        expected = "equilateral"
        s = Solution()
        result = s.triangleType(nums)
        assert result == expected
