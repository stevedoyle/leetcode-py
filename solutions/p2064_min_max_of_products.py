# Title: Minimized Maximum of Products Distributed to Any Store
# URL: https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
# Difficulty: Medium

from typing import List
import heapq
import math


class Solution:
    def minimizedMaximum(self, n, quantities):
        m = len(quantities)

        # Create a list of tuples (-ratio, quantity, stores_assigned)
        type_store_pairs = [(-q, q, 1) for q in quantities]

        # Use heapq.heapify() to convert the list into a heap in O(m) time
        heapq.heapify(type_store_pairs)

        # Iterate over the remaining n - m stores
        for _ in range(n - m):
            # Pop the element with the maximum ratio (due to negative sign it's min-heap)
            (
                neg_ratio,
                total_quantity_of_type,
                stores_assigned_to_type,
            ) = heapq.heappop(type_store_pairs)

            # Calculate the new ratio after assigning one more store
            new_stores_assigned_to_type = stores_assigned_to_type + 1
            new_ratio = total_quantity_of_type / new_stores_assigned_to_type

            # Push the updated pair back into the heap
            heapq.heappush(
                type_store_pairs,
                (
                    -new_ratio,
                    total_quantity_of_type,
                    new_stores_assigned_to_type,
                ),
            )

        # Pop the first element to get the final ratio
        _, total_quantity_of_type, stores_assigned_to_type = heapq.heappop(
            type_store_pairs
        )

        # Return the maximum minimum ratio
        return math.ceil(total_quantity_of_type / stores_assigned_to_type)


class TestMinMax:
    def test_example1(self):
        n = 6
        quantities = [11, 6]
        expected = 3
        assert Solution().minimizedMaximum(n, quantities) == expected

    def test_example2(self):
        n = 7
        quantities = [15, 10, 10]
        expected = 5
        assert Solution().minimizedMaximum(n, quantities) == expected

    def test_example3(self):
        n = 1
        quantities = [100000]
        expected = 100000
        assert Solution().minimizedMaximum(n, quantities) == expected
