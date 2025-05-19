from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == (total_sum - left_sum - num):
                return i
            left_sum += num

        return -1


class TestPivotIndex:
    def test_example1(self):
        nums = [1, 7, 3, 6, 5, 6]
        expected = 3
        s = Solution()
        result = s.pivotIndex(nums)
        assert result == expected

    def test_example2(self):
        nums = [1, 2, 3]
        expected = -1
        s = Solution()
        result = s.pivotIndex(nums)
        assert result == expected

    def test_example3(self):
        nums = [2, 1, -1]
        expected = 0
        s = Solution()
        result = s.pivotIndex(nums)
        assert result == expected
