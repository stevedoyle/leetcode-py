# Title: Implement Stack using Queues
# URL: https://leetcode.com/problems/implement-stack-using-queues/
# Difficulty: Easy


class MyStack:
    def __init__(self):
        self.queue = []
        self.aux = []
        self.top_val = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.top_val = x

    def pop(self) -> int:
        while len(self.queue) > 1:
            self.aux.append(self.queue.pop(0))
        res = self.queue.pop(0)
        self.queue, self.aux = self.aux, self.queue
        self.top_val = self.queue[-1] if self.queue else 0
        return res

    def top(self) -> int:
        return self.top_val

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


class TestMyStack:
    def test_example1(self):
        my_stack = MyStack()
        my_stack.push(1)
        my_stack.push(2)
        assert my_stack.top() == 2
        assert my_stack.pop() == 2
        assert not my_stack.empty()
