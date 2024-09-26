class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        """Optimized solution"""
        # Binary search to find where the new booking should be inserted
        idx = self.search(start)

        if idx > 0 and start < self.calendar[idx - 1][1]:
            # This booking starts before the previous booking ends
            return False

        if idx < len(self.calendar) and end > self.calendar[idx][0]:
            # This booking ends after the next booking starts
            return False

        # Insert the new booking
        # Keep calendar sorted by start time
        self.calendar.insert(idx, (start, end))
        return True

    def search(self, start) -> int:
        """Binary search to find where the new booking should be inserted"""
        left, right = 0, len(self.calendar)
        while left < right:
            mid = (left + right) // 2
            if self.calendar[mid][0] >= start:
                right = mid
            else:
                left = mid + 1
        return left

    # Time: O(n^2) for n bookings, Space: O(n)
    def book_slow(self, start: int, end: int) -> bool:
        """Brute force solution"""
        for s, e in self.calendar:
            if start < e and end > s:
                return False
        self.calendar.append((start, end))
        return True


class TestMyCalendar:
    def test_example1(self):
        calendar = MyCalendar()
        assert calendar.book(10, 20)
        assert not calendar.book(15, 25)
        assert calendar.book(20, 30)

    def test_example1_slow(self):
        calendar = MyCalendar()
        assert calendar.book_slow(10, 20)
        assert not calendar.book_slow(15, 25)
        assert calendar.book_slow(20, 30)
