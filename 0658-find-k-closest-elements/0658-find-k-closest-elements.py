class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        L = 0
        R = len(arr) - 1

        while (R - L + 1 > k):
            if (self.isCloser(arr[L], arr[R], x)):
                R -= 1
            else:
                L += 1
        return arr[L:R + 1]

    def isCloser(self, a, b, x):
        if (abs(a - x) == abs(b - x)):
            return True if a < b else False
        elif (abs(a - x) < abs(b - x)):
            return True
        else:
            return False
