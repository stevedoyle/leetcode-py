# Title: Merge k Sorted Lists
# URL: https://leetcode.com/problems/merge-k-sorted-lists/
# Difficulty: Hard

from utils import ListNode, create_linked_list

from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge_two_lists(
            l1: Optional[ListNode], l2: Optional[ListNode]
        ) -> Optional[ListNode]:
            if not l1:
                return l2
            if not l2:
                return l1

            if l1.val < l2.val:
                l1.next = merge_two_lists(l1.next, l2)
                return l1
            else:
                l2.next = merge_two_lists(l1, l2.next)
                return l2

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    merged_lists.append(merge_two_lists(lists[i], lists[i + 1]))
                else:
                    merged_lists.append(lists[i])
            lists = merged_lists

        return lists[0]


class TestMergeKLists:
    def test_example1(self):
        lists = [
            create_linked_list([1, 4, 5]),
            create_linked_list([1, 3, 4]),
            create_linked_list([2, 6]),
        ]
        expected = create_linked_list([1, 1, 2, 3, 4, 4, 5, 6])
        assert Solution().mergeKLists(lists) == expected

    def test_example2(self):
        lists = []
        expected = None
        assert Solution().mergeKLists(lists) == expected

    def test_example3(self):
        lists = [None]
        expected = None
        assert Solution().mergeKLists(lists) == expected
