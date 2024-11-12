# Title: Most Beautiful Item for Each Query
# URL: https://leetcode.com/problems/most-beautiful-item-for-each-query/
# Difficulty: Medium

from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        result = [0] * len(queries)

        items.sort(key=lambda x: x[0])

        queries_with_indices = [[queries[i], i] for i in range(len(queries))]
        queries_with_indices.sort(key=lambda x: x[0])

        item_idx = 0
        max_beauty = 0

        for q, idx in queries_with_indices:
            while item_idx < len(items) and items[item_idx][0] <= q:
                max_beauty = max(max_beauty, items[item_idx][1])
                item_idx += 1

            if max_beauty == 0:
                continue

            result[idx] = max_beauty

        return result


class TestMaxBeauty:
    def test_example1(self):
        items = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]
        queries = [1, 2, 3, 4, 5, 6]
        expected = [2, 4, 5, 5, 6, 6]
        assert Solution().maximumBeauty(items, queries) == expected

    def test_example2(self):
        items = [[1, 2], [1, 2], [1, 3], [1, 4]]
        queries = [1]
        expected = [4]
        assert Solution().maximumBeauty(items, queries) == expected

    def test_example3(self):
        items = [[10, 1000]]
        queries = [5]
        expected = [0]
        assert Solution().maximumBeauty(items, queries) == expected
