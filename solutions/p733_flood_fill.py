# Title: Flood Fill
# URL: https://leetcode.com/problems/flood-fill/
# Difficulty: Easy

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image

        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r >= len(image)
                or c >= len(image[0])
                or image[r][c] != original_color
            ):
                return
            image[r][c] = color
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        dfs(sr, sc)
        return image


class TestFloodFill:
    def test_example1(self):
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr = 1
        sc = 1
        newColor = 2
        expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        s = Solution()
        assert s.floodFill(image, sr, sc, newColor) == expected

    def test_example2(self):
        image = [[0, 0, 0], [0, 1, 1]]
        sr = 1
        sc = 1
        newColor = 1
        expected = [[0, 0, 0], [0, 1, 1]]
        s = Solution()
        assert s.floodFill(image, sr, sc, newColor) == expected
