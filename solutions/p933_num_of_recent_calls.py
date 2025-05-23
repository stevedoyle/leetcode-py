from collections import deque


class RecentCounter:

    def __init__(self):
        self.pings = deque()

    def ping(self, t: int) -> int:
        self.pings.append(t)
        while self.pings and self.pings[0] < t - 3000:
            self.pings.popleft()
        return len(self.pings)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


class TestRecentCounter:
    def test_example1(self):
        recent_counter = RecentCounter()
        assert recent_counter.ping(1) == 1
        assert recent_counter.ping(100) == 2
        assert recent_counter.ping(3001) == 3
        assert recent_counter.ping(3002) == 3
