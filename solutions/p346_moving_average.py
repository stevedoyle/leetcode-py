from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.window = deque()
        self.size = size
        self.win_sum = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.win_sum += val
        if len(self.window) > self.size:
            self.win_sum -= self.window.popleft()
        return self.win_sum / float(len(self.window))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


class TestMovingAverage:
    def test_moving_average(self):
        # Test case 1: Basic functionality
        ma = MovingAverage(3)
        assert ma.next(1) == 1.0
        assert ma.next(10) == 5.5
        assert ma.next(3) == 4.666666666666667
        assert ma.next(5) == 6.0

        # Test case 2: Window size of 1
        ma = MovingAverage(1)
        assert ma.next(5) == 5.0
        assert ma.next(10) == 10.0

        # Test case 3: Window size larger than the number of elements added
        ma = MovingAverage(5)
        assert ma.next(1) == 1.0
        assert ma.next(2) == 1.5
