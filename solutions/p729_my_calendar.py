class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.calendar:
            if start < e and end > s:
                return False
        self.calendar.append((start, end))
        return True


class TestMyCalendar:
    def test_example1(self):
        calendar = MyCalendar()
        assert calendar.book(10, 20) == True
        assert calendar.book(15, 25) == False
        assert calendar.book(20, 30) == True
