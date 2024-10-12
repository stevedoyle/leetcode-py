# Title: Reverse Polish Notation
# URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Difficulty: Medium

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]


class TestReversePolish:
    def test_example1(self):
        tokens = ["2", "1", "+", "3", "*"]
        assert Solution().evalRPN(tokens) == 9

    def test_example2(self):
        tokens = ["4", "13", "5", "/", "+"]
        assert Solution().evalRPN(tokens) == 6

    def test_example3(self):
        tokens = ["10", "6", "9", "3", "/", "-11", "*", "/", "*", "17", "+", "5", "+"]
        assert Solution().evalRPN(tokens) == 22
