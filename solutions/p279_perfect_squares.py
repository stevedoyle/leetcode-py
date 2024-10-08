# Title: Perfect Squares
# URL: https://leetcode.com/problems/perfect-squares/
# Difficulty: Medium


class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, int(n**0.5) + 1)]
        queue = {n}
        level = 0

        while queue:
            level += 1
            new_queue = set()
            for remainder in queue:
                for square in squares:
                    if remainder == square:
                        return level
                    elif remainder < square:
                        break
                    else:
                        new_queue.add(remainder - square)
            queue = new_queue
        return level


class TestNumSquares:
    def test_example1(self):
        n = 12
        expected = 3
        assert Solution().numSquares(n) == expected

    def test_example2(self):
        n = 13
        expected = 2
        assert Solution().numSquares(n) == expected
