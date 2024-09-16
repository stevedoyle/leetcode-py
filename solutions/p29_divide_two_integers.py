# Link: https://leetcode.com/problems/divide-two-integers/
# Difficulty: Medium


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if dividend == -(2**31):
            if divisor == -1:
                return 2**31 - 1
            else:
                return dividend
        elif dividend > 2**31 - 1:
            return 2**31 - 1

        sign = 1 if dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)

        result = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                result += i
                i <<= 1
                temp <<= 1

        return sign * result


class TestDivideTwoIntegers:
    def test_example1(self):
        dividend = 10
        divisor = 3

        assert Solution().divide(dividend, divisor) == 3

    def test_example2(self):
        dividend = 7
        divisor = -3

        assert Solution().divide(dividend, divisor) == -2

    def test_example3(self):
        dividend = 0
        divisor = 1

        assert Solution().divide(dividend, divisor) == 0

    def test_example4(self):
        dividend = 15
        divisor = 3

        assert Solution().divide(dividend, divisor) == 5
