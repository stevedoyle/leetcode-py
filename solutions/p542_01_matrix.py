# Title: 01 Matrix
# URL: https://leetcode.com/problems/01-matrix/
# Difficulty: Medium

from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        dist = [[0] * cols for _ in range(rows)]
        q = []
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    dist[i][j] = float("inf")
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            i, j = q.pop(0)
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if ni < 0 or nj < 0 or ni >= rows or nj >= cols:
                    continue
                if dist[ni][nj] > dist[i][j] + 1:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
        return dist


class TestUpdateMatrix:
    def test_example1(self):
        mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        s = Solution()
        result = s.updateMatrix(mat)
        assert result == expected

    def test_example2(self):
        mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
        expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        s = Solution()
        result = s.updateMatrix(mat)
        assert result == expected
