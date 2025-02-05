class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class TestMinStack:
    def test_example1(self):
        obj = MinStack()
        obj.push(-2)
        obj.push(0)
        obj.push(-3)
        assert obj.getMin() == -3
        obj.pop()
        assert obj.top() == 0
        assert obj.getMin() == -2
