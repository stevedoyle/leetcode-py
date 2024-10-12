# Title: Implement Queue using Stacks
# URL: https://leetcode.com/problems/implement-queue-using-stacks/
# Difficulty: Easy


class MyQueue:
    def __init__(self):
        self.stack = []
        self.aux = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
        else:
            while self.stack:
                self.aux.append(self.stack.pop())
            self.stack.append(x)
            while self.aux:
                self.stack.append(self.aux.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


class TestMyQueue:
    def test_example1(self):
        obj = MyQueue()
        obj.push(1)
        obj.push(2)
        assert obj.peek() == 1
        assert obj.pop() == 1
        assert not obj.empty()

    def test_example2(self):
        obj = MyQueue()
        obj.push(1)
        obj.push(2)
        obj.pop()
        obj.push(3)
        assert obj.peek() == 2
        assert obj.pop() == 2
        assert not obj.empty()
        assert obj.pop() == 3
        assert obj.empty()
