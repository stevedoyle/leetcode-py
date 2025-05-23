class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            stack = []
            for c in s:
                if c == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return "".join(stack)

        return build(s) == build(t)


class TestBackspaceStringCompare:
    def test_backspace_compare(self):
        solution = Solution()
        assert solution.backspaceCompare("ab#c", "ad#c")
        assert solution.backspaceCompare("ab##", "c#d#")
        assert solution.backspaceCompare("a##c", "#a#c")
        assert not solution.backspaceCompare("a#c", "b")
        assert solution.backspaceCompare("xywrrmp", "xywrrmu#p")
