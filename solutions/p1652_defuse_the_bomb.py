# Title: Defuse the Bomb
# URL: https://leetcode.com/problems/defuse-the-bomb/
# Difficulty: Easy

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        elif k > 0:
            result = []
            for i in range(n):
                if i + k < n:
                    total = sum(code[i + 1 : i + k + 1])
                else:
                    total = sum(code[i + 1 :]) + sum(code[: k - (n - i) + 1])
                result.append(total)
            return result
        elif k < 0:
            result = []
            for i in range(n):
                if i + k >= 0:
                    total = sum(code[i + k : i])
                else:
                    total = sum(code[i + k :]) + sum(code[:i])
                result.append(total)
            return result
        return []


class TestDecrypt:
    def test_example1(self):
        code = [5, 7, 1, 4]
        k = 3
        expected = [12, 10, 16, 13]
        assert Solution().decrypt(code, k) == expected

    def test_example2(self):
        code = [1, 2, 3, 4]
        k = 0
        expected = [0, 0, 0, 0]
        assert Solution().decrypt(code, k) == expected

    def test_example3(self):
        code = [2, 4, 9, 3]
        k = -2
        expected = [12, 5, 6, 13]
        assert Solution().decrypt(code, k) == expected
