# Title: Rotate Array
# URL: https://leetcode.com/problems/rotate-array/
# Difficulty: Medium


from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums.pop())


class TestRotate:
    def test_example1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        expected = [5, 6, 7, 1, 2, 3, 4]

        s = Solution()
        s.rotate(nums, k)

        assert nums == expected

    def test_example2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        expected = [3, 99, -1, -100]

        s = Solution()
        s.rotate(nums, k)

        assert nums == expected

    def test_rotate2_example1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        expected = [5, 6, 7, 1, 2, 3, 4]

        s = Solution()
        s.rotate2(nums, k)

        assert nums == expected

    def test_rotate2_example2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        expected = [3, 99, -1, -100]

        s = Solution()
        s.rotate2(nums, k)

        assert nums == expected
