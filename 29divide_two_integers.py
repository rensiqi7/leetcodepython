class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = 1
        MAX = 2**31 - 1
        MIN = -2**31
        if dividend == MIN and divisor == -1:
            return MAX

        if dividend < 0:
            flag *= -1
            dividend = -dividend
        if divisor < 0:
            flag *= -1
            divisor = -divisor
        if dividend - divisor < 0:
            return 0
        if divisor == 1:
            return flag * dividend
        res = 0
        cnt = 1
        div = divisor
        while dividend - div >= 0:
            while dividend - div >= 0:
                cnt += cnt
                div += div
            cnt >>= 1
            div >>= 1
            dividend -= div
            if cnt > MAX - res:
                return MAX
            res += cnt
            cnt = 1
            div = divisor
        return flag * res
