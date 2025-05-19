from typing import List
from collections import defaultdict


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_map = defaultdict(int)
        min_pickup = len(cards) + 1

        for i, card in enumerate(cards):
            if card in card_map:
                min_pickup = min(min_pickup, i - card_map[card] + 1)
            card_map[card] = i

        return min_pickup if min_pickup != len(cards) + 1 else -1


class TestMinimumCardPickup:
    def test_example1(self):
        cards = [3, 4, 2, 3, 4, 7]
        expected = 4
        s = Solution()
        result = s.minimumCardPickup(cards)
        assert result == expected

    def test_example2(self):
        cards = [1, 0, 5, 3]
        expected = -1
        s = Solution()
        result = s.minimumCardPickup(cards)
        assert result == expected

    def test_example3(self):
        cards = [1, 2, 3, 4, 5, 2]
        expected = 5
        s = Solution()
        result = s.minimumCardPickup(cards)
        assert result == expected
