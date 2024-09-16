# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)

# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [1]
# Output: [1]

# Constraints:
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node


# Add a few test cases


class TestSwapPairs:
    # Test case 1
    def test_swapPairs_2_groups(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        result = Solution().swapPairs(head)
        assert result.val == 2
        assert result.next.val == 1
        assert result.next.next.val == 4
        assert result.next.next.next.val == 3
        assert result.next.next.next.next == None

    # Test case 2
    def test_swapPairs_empty_list(self):
        head = None
        result = Solution().swapPairs(head)
        assert result == None

    # Test case 3
    def test_swapPairs_single_element_list(self):
        head = ListNode(1)
        result = Solution().swapPairs(head)
        assert result.val == 1
        assert result.next == None

    # Test case 4
    def test_swapPairs_1_pair(self):
        head = ListNode(1, ListNode(2))
        result = Solution().swapPairs(head)
        assert result.val == 2
        assert result.next.val == 1
        assert result.next.next == None

    # Test case 5
    def test_swapPairs_incomplete_pair(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        result = Solution().swapPairs(head)
        assert result.val == 2
        assert result.next.val == 1
        assert result.next.next.val == 3
        assert result.next.next.next == None

    # Test case 6
    def test_swapPairs_incomplete_pair22(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = Solution().swapPairs(head)
        assert result.val == 2
        assert result.next.val == 1
        assert result.next.next.val == 4
        assert result.next.next.next.val == 3
        assert result.next.next.next.next.val == 5
        assert result.next.next.next.next.next == None
