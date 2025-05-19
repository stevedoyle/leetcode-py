from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


class TestContainsDuplicate:
    def test_example1(self):
        nums = [1, 2, 3, 1]
        expected = True
        s = Solution()
        result = s.containsDuplicate(nums)
        assert result == expected

    def test_example2(self):
        nums = [1, 2, 3, 4]
        expected = False
        s = Solution()
        result = s.containsDuplicate(nums)
        assert result == expected

    def test_example3(self):
        nums = [1, 2, 3, 1, 2, 3]
        expected = True
        s = Solution()
        result = s.containsDuplicate(nums)
        assert result == expected
