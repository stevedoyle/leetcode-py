from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_cities = set()
        end_cities = set()

        for path in paths:
            start_cities.add(path[0])
            end_cities.add(path[1])

        for city in end_cities:
            if city not in start_cities:
                return city
        return ""


class TestDestinationCity:
    def test_example1(self):
        paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
        expected = "Sao Paulo"
        s = Solution()
        result = s.destCity(paths)
        assert result == expected

    def test_example2(self):
        paths = [["B", "C"], ["D", "B"], ["C", "A"]]
        expected = "A"
        s = Solution()
        result = s.destCity(paths)
        assert result == expected

    def test_example3(self):
        paths = [["A", "Z"]]
        expected = "Z"
        s = Solution()
        result = s.destCity(paths)
        assert result == expected
