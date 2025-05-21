from typing import Optional
from utils import ListNode, create_linked_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, head)

        prev = sentinel

        while head:
            # If its the beginning of a duplicates sequence
            # skip all duplicates
            if head.next and head.val == head.next.val:
                # Skip all duplicates
                while head.next and head.val == head.next.val:
                    head = head.next
                # Remove the duplicates
                prev.next = head.next
            else:
                prev = prev.next
            # Move to the next node
            head = head.next
        return sentinel.next


class TestDeleteDuplicates:
    def test_example1(self):
        head = create_linked_list([1, 2, 3, 3, 4, 4, 5])
        expected = create_linked_list([1, 2, 5])
        s = Solution()
        result = s.deleteDuplicates(head)
        assert (result.to_list() if result else None) == (
            expected.to_list() if expected else None
        )

    def test_example2(self):
        head = create_linked_list([1, 1, 1, 2, 3])
        expected = create_linked_list([2, 3])
        s = Solution()
        result = s.deleteDuplicates(head)
        assert (result.to_list() if result else None) == (
            expected.to_list() if expected else None
        )
