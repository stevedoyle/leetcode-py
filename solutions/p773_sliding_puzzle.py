# Title: 773. Sliding Puzzle
# URL: https://leetcode.com/problems/sliding-puzzle/
# Difficulty: Hard

from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = [[1, 2, 3], [4, 5, 0]]
        start = []
        for i in range(2):
            for j in range(3):
                start.append(board[i][j])
        start = tuple(start)
        target = tuple([1, 2, 3, 4, 5, 0])
        queue = [start]
        visited = set()
        visited.add(start)
        step = 0
        while queue:
            next_queue = []
            for cur in queue:
                if cur == target:
                    return step
                zero = cur.index(0)
                for d in [-1, 1, -3, 3]:
                    if zero + d < 0 or zero + d >= 6:
                        continue
                    if zero == 2 and d == 1 or zero == 3 and d == -1:
                        continue
                    next_board = list(cur)
                    next_board[zero], next_board[zero + d] = (
                        next_board[zero + d],
                        next_board[zero],
                    )
                    next_board = tuple(next_board)
                    if next_board not in visited:
                        visited.add(next_board)
                        next_queue.append(next_board)
            queue = next_queue
            step += 1

        return -1


class TestSlidingPuzzle:
    def test_example1(self):
        board = [[1, 2, 3], [4, 0, 5]]
        assert Solution().slidingPuzzle(board) == 1

    def test_example2(self):
        board = [[1, 2, 3], [5, 4, 0]]
        assert Solution().slidingPuzzle(board) == -1

    def test_example3(self):
        board = [[4, 1, 2], [5, 0, 3]]
        assert Solution().slidingPuzzle(board) == 5
