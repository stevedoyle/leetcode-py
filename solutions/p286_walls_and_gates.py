# Title: Walls and Gates
# Link: https://leetcode.com/problems/walls-and-gates/
# Difficulty: Medium

from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = []
        # find the gates and add them to the queue
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        # start from the gates and update the distance to the nearest gate
        # for each of the surrounding rooms.
        while queue:
            i, j = queue.pop(0)
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if (
                    0 <= x < len(rooms)
                    and 0 <= y < len(rooms[0])
                    and rooms[x][y] == 2147483647
                ):
                    rooms[x][y] = rooms[i][j] + 1
                    queue.append((x, y))


class TestWallsAndGates:
    def test_example1(self):
        rooms = [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647],
        ]
        expected = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
        solution = Solution()
        solution.wallsAndGates(rooms)
        assert rooms == expected

    def test_example2(self):
        rooms = [[-1]]
        expected = [[-1]]
        solution = Solution()
        solution.wallsAndGates(rooms)
        assert rooms == expected
