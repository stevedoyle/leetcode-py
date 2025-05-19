from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        prefix_mod = 0
        mod_seen = {0: -1}

        for i, num in enumerate(nums):
            prefix_mod = (prefix_mod + num) % k

            if prefix_mod in mod_seen:
                if i - mod_seen[prefix_mod] > 1:
                    return True
            else:
                mod_seen[prefix_mod] = i
        return False


class TestCheckSubarraySum:
    def test_example1(self):
        nums = [23, 2, 4, 6, 7]
        k = 6
        expected = True
        s = Solution()
        result = s.checkSubarraySum(nums, k)
        assert result == expected

    def test_example2(self):
        nums = [23, 2, 6, 4, 7]
        k = 13
        expected = False
        s = Solution()
        result = s.checkSubarraySum(nums, k)
        assert result == expected
