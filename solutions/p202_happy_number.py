class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit**2
            return total_sum

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


class TestIsHappy:
    def test_example1(self):
        n = 19
        assert Solution().isHappy(n)

    def test_example2(self):
        n = 2
        assert not Solution().isHappy(n)
