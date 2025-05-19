class Solution:
    def isPathCrossing(self, path: str) -> bool:
        start = (0, 0)
        visited: set[tuple[int, int]] = {start}
        directions = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
        for move in path:
            dx, dy = directions[move]
            start = (start[0] + dx, start[1] + dy)
            if start in visited:
                return True
            visited.add(start)
        return False


class TestIsPathCrossing:
    def test_example1(self):
        path = "NES"
        expected = False
        s = Solution()
        result = s.isPathCrossing(path)
        assert result == expected

    def test_example2(self):
        path = "NESWW"
        expected = True
        s = Solution()
        result = s.isPathCrossing(path)
        assert result == expected

    def test_example3(self):
        path = "NNEESSWW"
        expected = True
        s = Solution()
        result = s.isPathCrossing(path)
        assert result == expected
