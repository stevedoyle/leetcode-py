# Title: 224. Basic Calculator
# URL: https://leetcode.com/problems/basic-calculator/
# Difficulty: Hard


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        operand = 0
        sign = 1

        for c in s:
            if c.isdigit():
                operand = operand * 10 + int(c)
            elif c == "+":
                result += sign * operand
                sign = 1
                operand = 0
            elif c == "-":
                result += sign * operand
                sign = -1
                operand = 0
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif c == ")":
                result += sign * operand
                result *= stack.pop()
                result += stack.pop()
                operand = 0
        return result + sign * operand


class TestCalculate:
    def test_example1(self):
        s = "1 + 1"
        assert Solution().calculate(s) == 2

    def test_example2(self):
        s = " 2-1 + 2 "
        assert Solution().calculate(s) == 3

    def test_example3(self):
        s = "(1+(4+5+2)-3)+(6+8)"
        assert Solution().calculate(s) == 23
