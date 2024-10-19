# Title: Find Kth Bit in Nth Binary String
# URL: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
# Difficulty: Medium


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for _ in range(n - 1):
            s += "1" + "".join("1" if c == "0" else "0" for c in s[::-1])
        return s[k - 1]

    def findKthBit2(self, n: int, k: int) -> str:
        s = "0"
        for _ in range(n - 1):
            print(s)
            add = "1"
            for c in s[::-1]:
                if c == "0":
                    add += "1"
                else:
                    add += "0"
            s += add

        return s[k - 1]


class TestFindKthBit:
    def test_example1(self):
        n = 3
        k = 1
        expected = "0"
        s = Solution()
        assert s.findKthBit(n, k) == expected
        assert s.findKthBit2(n, k) == expected

    def test_example2(self):
        n = 4
        k = 11
        expected = "1"
        s = Solution()
        assert s.findKthBit(n, k) == expected
        assert s.findKthBit2(n, k) == expected
