# Title: My Calendar II
# URL: https://leetcode.com/problems/my-calendar-ii/
# Difficulty: Medium


class MyCalendarTwo:
    def __init__(self):
        self.bookings = []
        self.overlap_bookings = []

    def book(self, start: int, end: int) -> bool:
        # Check if the new booking overlaps with any double-booked booking.
        for booking in self.overlap_bookings:
            if self.does_overlap(booking[0], booking[1], start, end):
                return False

        # Add any new double overlaps that the current booking creates.
        for booking in self.bookings:
            if self.does_overlap(booking[0], booking[1], start, end):
                self.overlap_bookings.append(
                    self.get_overlapped(booking[0], booking[1], start, end)
                )

        # Add the new booking to the list of bookings.
        self.bookings.append((start, end))
        return True

    # Return True if the booking [start1, end1) & [start2, end2) overlaps.
    def does_overlap(self, start1: int, end1: int, start2: int, end2: int) -> bool:
        return max(start1, start2) < min(end1, end2)

    # Return the overlapping booking between [start1, end1) & [start2, end2).
    def get_overlapped(self, start1: int, end1: int, start2: int, end2: int) -> tuple:
        return max(start1, start2), min(end1, end2)


class TestMyCalendarTwo:
    def test_example1(self):
        calendar = MyCalendarTwo()
        assert calendar.book(10, 20)
        assert calendar.book(50, 60)
        assert calendar.book(10, 40)
        assert not calendar.book(5, 15)
        assert calendar.book(5, 10)
        assert calendar.book(25, 55)
