class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


class TestRemoveDuplicates:
    def test_remove_duplicates(self):
        solution = Solution()
        # Test case 1: Simple case with duplicates
        assert solution.removeDuplicates("abbaca") == "ca"

        # Test case 2: No duplicates
        assert solution.removeDuplicates("abc") == "abc"

        # Test case 3: All characters are the same
        assert solution.removeDuplicates("aaaa") == ""

        # Test case 4: Empty string
        assert solution.removeDuplicates("") == ""

        # Test case 5: Alternating characters
        assert solution.removeDuplicates("abccba") == ""
