class MinStack:

    def __init__(self):
        self.stack = []  # Stores tuples of (value, min_value)

    def push(self, val: int) -> None:
        curr_min = min(self.stack[-1][1], val) if self.stack else val
        self.stack.append((val, curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else -1

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else -1


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
