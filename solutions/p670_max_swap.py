# Title: 670. Maximum Swap
# URL: https://leetcode.com/problems/maximum-swap/
# Difficulty: Medium


class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        n = len(num_list)
        max_right_idx = [0] * n

        max_right_idx[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            if num_list[i] > num_list[max_right_idx[i + 1]]:
                max_right_idx[i] = i
            else:
                max_right_idx[i] = max_right_idx[i + 1]

        for i in range(n):
            if num_list[i] < num_list[max_right_idx[i]]:
                num_list[i], num_list[max_right_idx[i]] = (
                    num_list[max_right_idx[i]],
                    num_list[i],
                )
                return int("".join(num_list))

        return num


class TestMaxSwap:
    def test_example1(self):
        num = 2736
        expected = 7236

        solution = Solution()
        assert solution.maximumSwap(num) == expected

    def test_example2(self):
        num = 9973
        expected = 9973

        solution = Solution()
        assert solution.maximumSwap(num) == expected

    def test_example3(self):
        num = 98368
        expected = 98863

        solution = Solution()
        assert solution.maximumSwap(num) == expected
