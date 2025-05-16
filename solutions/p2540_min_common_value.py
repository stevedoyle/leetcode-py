from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Given two integer arrays nums1 and nums2, return the minimum integer common to both arrays, or -1 if there is no common integer.
        """
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1


class TestGetCommon:
    def test_example1(self):
        nums1 = [1, 2, 3]
        nums2 = [2, 4]
        expected = 2
        s = Solution()
        result = s.getCommon(nums1, nums2)
        assert result == expected

    def test_example2(self):
        nums1 = [1, 2, 3, 6]
        nums2 = [2, 3, 4, 5]
        expected = 2
        s = Solution()
        result = s.getCommon(nums1, nums2)
        assert result == expected

    def test_example3(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5]
        expected = -1
        s = Solution()
        result = s.getCommon(nums1, nums2)
        assert result == expected
