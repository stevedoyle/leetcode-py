# Title: Merge Sorted Array
# URL: https://leetcode.com/problems/merge-sorted-array/
# Difficulty: Easy

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Create a copy of nums1
        nums1_copy = nums1[:m]

        nums1.clear()

        # Initialize pointers for nums1_copy and nums2
        p1 = 0
        p2 = 0

        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # If there are remaining elements in nums1_copy
        if p1 < m:
            nums1.extend(nums1_copy[p1:])
        # If there are remaining elements in nums2
        if p2 < n:
            nums1.extend(nums2[p2:])


class TestMergeSortedArray:
    def test_example_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        Solution().merge(nums1, m, nums2, n)
        assert [1, 2, 2, 3, 5, 6] == nums1

    def test_example_2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        Solution().merge(nums1, m, nums2, n)
        assert [1] == nums1

    def test_example_3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        Solution().merge(nums1, m, nums2, n)
        assert [1] == nums1

    def test_example_4(self):
        nums1 = [4, 5, 6, 0, 0, 0]
        m = 3
        nums2 = [1, 2, 3]
        n = 3
        Solution().merge(nums1, m, nums2, n)
        assert [1, 2, 3, 4, 5, 6] == nums1

    def test_example_5(self):
        nums1 = [1, 2, 4, 5, 6, 0]
        m = 5
        nums2 = [3]
        n = 1
        Solution().merge(nums1, m, nums2, n)
        assert [1, 2, 3, 4, 5, 6] == nums1
