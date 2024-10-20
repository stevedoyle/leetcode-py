# Title: Parsing A Boolean Expression
# URL: https://leetcode.com/problems/parsing-a-boolean-expression/
# Difficulty: Hard


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for char in expression:
            if char == ")":
                seen = set()
                while stack[-1] != "(":
                    seen.add(stack.pop())
                stack.pop()
                operator = stack.pop()
                if operator == "&":
                    if "f" in seen:
                        stack.append("f")
                    else:
                        stack.append("t")
                elif operator == "|":
                    if "t" in seen:
                        stack.append("t")
                    else:
                        stack.append("f")
                elif operator == "!":
                    v = seen.pop()
                    if v == "t":
                        stack.append("f")
                    else:
                        stack.append("t")
            elif char != ",":
                stack.append(char)

        if stack[0] == "t":
            return True

        return False


class TestParseBoolExpr:
    def test_example1(self):
        expression = "&(|(f))"
        assert not Solution().parseBoolExpr(expression)

    def test_example2(self):
        expression = "|(f,f,f,t)"
        assert Solution().parseBoolExpr(expression)
