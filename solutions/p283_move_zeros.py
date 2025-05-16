from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:  # noqa: F821
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] != 0:
                i += 1
                if i == j:
                    j += 1
                continue
            if nums[j] == 0:
                j += 1
                continue
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1


class TestMoveZeroes:
    def test_example1(self):
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        s = Solution()
        s.moveZeroes(nums)
        assert nums == expected

    def test_example2(self):
        nums = [0]
        expected = [0]
        s = Solution()
        s.moveZeroes(nums)
        assert nums == expected
