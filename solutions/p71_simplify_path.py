# Title: Simplify Path
# URL: https://leetcode.com/problems/simplify-path/
# Difficulty: Medium


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for directory in path.split("/"):
            if directory == "..":
                stack = stack[:-1]
            elif directory and directory != ".":
                stack.append(directory)

        return "/" + "/".join(stack)


class TestSimplifyPath:
    def test_example1(self):
        path = "/home/"
        expected = "/home"
        solution = Solution()
        assert solution.simplifyPath(path) == expected

    def test_example2(self):
        path = "/home//foo/"
        expected = "/home/foo"
        solution = Solution()
        assert solution.simplifyPath(path) == expected

    def test_example3(self):
        path = "/home/user/Documents/../Pictures"
        expected = "/home/user/Pictures"
        solution = Solution()
        assert solution.simplifyPath(path) == expected

    def test_example4(self):
        path = "/../"
        expected = "/"
        solution = Solution()
        assert solution.simplifyPath(path) == expected

    def test_example5(self):
        path = "/.../a/../b/c/../d/./"
        expected = "/.../b/d"
        solution = Solution()
        assert solution.simplifyPath(path) == expected
