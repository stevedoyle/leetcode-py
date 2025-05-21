from typing import Optional
from utils import ListNode, create_linked_list


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr == arr[::-1]


class TestIsPalindrome:
    def test_is_palindrome(self):
        solution = Solution()
        # Test case 1: Odd-length palindrome
        head = create_linked_list([1, 2, 3, 2, 1])
        assert solution.isPalindrome(head) == True

        # Test case 2: Even-length palindrome
        head = create_linked_list([1, 2, 2, 1])
        assert solution.isPalindrome(head) == True

        # Test case 3: Not a palindrome
        head = create_linked_list([1, 2, 3, 4])
        assert solution.isPalindrome(head) == False

        # Test case 4: Single node (palindrome)
        head = create_linked_list([1])
        assert solution.isPalindrome(head) == True

        # Test case 5: Empty list (palindrome)
        head = create_linked_list([])
        assert solution.isPalindrome(head) == True
