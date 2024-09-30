# Title: Design a Stack With Increment Operation
# URL: https://leetcode.com/problems/design-a-stack-with-increment-operation/
# Difficulty: Medium


class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


class TestCustomStack:
    def test_example1(self):
        stk = CustomStack(3)
        stk.push(1)
        stk.push(2)
        assert stk.pop() == 2
        stk.push(2)
        stk.push(3)
        stk.push(4)
        stk.increment(5, 100)
        stk.increment(2, 100)
        assert stk.pop() == 103
        assert stk.pop() == 202
        assert stk.pop() == 201
        assert stk.pop() == -1
