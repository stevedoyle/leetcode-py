# Title: Remove Sub-Folders from the Filesystem
# URL: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
# Difficulty: Medium

from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        for f in folder:
            if not result or not f.startswith(result[-1] + "/"):
                result.append(f)
        return result


class TestRemoveSubfolders:
    def test_example1(self):
        folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
        expected = ["/a", "/c/d", "/c/f"]
        assert Solution().removeSubfolders(folder) == expected

    def test_example2(self):
        folder = ["/a", "/a/b/c", "/a/b/d"]
        expected = ["/a"]
        assert Solution().removeSubfolders(folder) == expected

    def test_example3(self):
        folder = ["/a/b/c", "/a/b/ca", "/a/b/d"]
        expected = ["/a/b/c", "/a/b/ca", "/a/b/d"]
        assert Solution().removeSubfolders(folder) == expected
