from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pt = [[1]]
        for _ in range(1, numRows):
            row = [1]
            for i in range(len(pt[-1]) - 1):
                row.append(pt[-1][i] + pt[-1][i + 1])
            row.append(1)
            pt.append(row)
        return pt


class TestPascalsTriangle:
    def test_example1(self):
        numRows = 5
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        assert Solution().generate(numRows) == expected

    def test_example2(self):
        numRows = 1
        expected = [[1]]
        assert Solution().generate(numRows) == expected
