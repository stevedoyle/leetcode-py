# Title: Valid Number
# URL: https://leetcode.com/problems/valid-number/
# Difficulty: Hard

import re


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        pattern = r"^[+-]?(\d+\.?|\.\d+)\d*([eE][+-]?\d+)?$"
        if re.search(pattern, s):
            return True

        return False

    def isNumberDfa(self, s: str) -> bool:
        dfa = [
            {"digit": 1, "sign": 2, "dot": 3},  # 0
            {"digit": 1, "dot": 4, "e": 5},  # 1
            {"digit": 1, "dot": 3},  # 2
            {"digit": 4},  # 3
            {"digit": 4, "e": 5},  # 4
            {"sign": 6, "digit": 7},  # 5
            {"digit": 7},  # 6
            {"digit": 7},  # 7
        ]

        state = 0
        for c in s:
            if c.isdigit():
                c = "digit"
            elif c in "+-":
                c = "sign"
            elif c == ".":
                c = "dot"
            elif c in "eE":
                c = "e"
            else:
                return False

            if c not in dfa[state]:
                return False

            state = dfa[state][c]
        return state in {1, 4, 7}


class TestIsNumber:
    def test_isNumber_regex(self):
        assert Solution().isNumber("0")
        assert not Solution().isNumber("e")
        assert not Solution().isNumber(".")
        assert Solution().isNumber(".1")
        assert Solution().isNumber("2")
        assert Solution().isNumber("0089")
        assert Solution().isNumber("-0")
        assert Solution().isNumber("+3")
        assert Solution().isNumber("5e2")
        assert Solution().isNumber("1E9")

    def test_isNumber_dfa(self):
        assert Solution().isNumberDfa("0")
        assert not Solution().isNumberDfa("e")
        assert not Solution().isNumberDfa(".")
        assert Solution().isNumberDfa(".1")
        assert Solution().isNumberDfa("2")
        assert Solution().isNumberDfa("0089")
        assert Solution().isNumberDfa("-0")
        assert Solution().isNumberDfa("+3")
        assert Solution().isNumberDfa("5e2")
        assert Solution().isNumberDfa("1E9")
