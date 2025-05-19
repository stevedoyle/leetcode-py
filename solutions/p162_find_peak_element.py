from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0

        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i

        if nums[-1] > nums[-2]:
            return len(nums) - 1
        return -1


class TestFindPeakElement:
    def test_example1(self):
        nums = [1, 2, 3, 1]
        expected = 2
        s = Solution()
        result = s.findPeakElement(nums)
        assert result == expected

    def test_example2(self):
        nums = [1, 2, 1, 3, 5, 6, 4]
        expected = [1, 5]
        s = Solution()
        result = s.findPeakElement(nums)
        assert result in expected

    def test_example3(self):
        nums = [1]
        expected = 0
        s = Solution()
        result = s.findPeakElement(nums)
        assert result == expected

    def test_example4(self):
        nums = [1, 2, 1]
        expected = 1
        s = Solution()
        result = s.findPeakElement(nums)
        assert result == expected
