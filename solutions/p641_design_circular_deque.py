class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.queue = []

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.queue:
            self.queue.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if self.queue:
            self.queue.pop()
            return True
        return False

    def getFront(self) -> int:
        if self.queue:
            return self.queue[0]
        return -1

    def getRear(self) -> int:
        if self.queue:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


class TestMyCircularDeque:
    def test_example_1(self):
        circularDeque = MyCircularDeque(3)
        assert circularDeque.insertLast(1)
        assert circularDeque.insertLast(2)
        assert circularDeque.insertFront(3)
        assert not circularDeque.insertFront(4)
        assert circularDeque.getRear()
        assert circularDeque.isFull()
        assert circularDeque.deleteLast()
        assert circularDeque.insertFront(4)
        assert circularDeque.getFront()
        assert circularDeque.getRear()
        assert circularDeque.deleteFront()
        assert circularDeque.getFront()
        assert not circularDeque.isEmpty()
        assert circularDeque.deleteLast()
        assert circularDeque.deleteFront()
        assert circularDeque.isEmpty()
