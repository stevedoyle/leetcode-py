# Title: Swapping Nodes in a Linked List
# URL: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# Difficulty: Medium

from typing import Optional

from utils import ListNode, create_linked_list


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        def get_node(node, index):
            for _ in range(index):
                node = node.next
            return node

        # Find the k-th node from the beginning
        first_kth = get_node(head, k - 1)

        # Find the k-th node from the end
        length = get_length(head)
        # 2nd kth distance from the beginning
        m = length - k + 1
        second_kth = get_node(head, m - 1)

        # Swap the values of the k-th node from the beginning and the k-th node from the end
        first_kth.val, second_kth.val = second_kth.val, first_kth.val

        return head


class TestSwapNodes:
    def test_example1(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        k = 2
        expected = create_linked_list([1, 4, 3, 2, 5])
        assert Solution().swapNodes(head, k) == expected

    def test_example2(self):
        head = create_linked_list([7, 9, 6, 6, 7, 8, 3, 0, 9, 5])
        k = 5
        expected = create_linked_list([7, 9, 6, 6, 8, 7, 3, 0, 9, 5])
        assert Solution().swapNodes(head, k) == expected

    def test_example3(self):
        head = create_linked_list([1])
        k = 1
        expected = create_linked_list([1])
        assert Solution().swapNodes(head, k) == expected

    def test_example4(self):
        head = create_linked_list([1, 2])
        k = 1
        expected = create_linked_list([2, 1])
        assert Solution().swapNodes(head, k) == expected
