# Title: 394. Decode String
# URL: https://leetcode.com/problems/decode-string/
# Difficulty: Medium


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        curr_str = ""

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append((num, curr_str))
                num = 0
                curr_str = ""
            elif c == "]":
                prev_num, prev_str = stack.pop()
                curr_str = prev_str + prev_num * curr_str
            else:
                curr_str += c

        return curr_str


class TestDecodeString:
    def test_example1(self):
        s = "3[a]2[bc]"
        assert Solution().decodeString(s) == "aaabcbc"

    def test_example2(self):
        s = "3[a2[c]]"
        assert Solution().decodeString(s) == "accaccacc"

    def test_example3(self):
        s = "2[abc]3[cd]ef"
        assert Solution().decodeString(s) == "abcabccdcdcdef"
