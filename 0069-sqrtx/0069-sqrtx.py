class Solution:
    def mySqrt(self, x: int) -> int:
        L = 0
        R = x / 2

        while L <= R:
            m = (L + R) // 2
            if m * m <= x and (m + 1) * (m + 1) >= x:
                if (m + 1) * (m + 1) == x:
                    return int(m + 1)
                else:
                    return int(m)
            elif m * m < x:
                L = m + 1
            elif m * m > x:
                R = m - 1

        return -1