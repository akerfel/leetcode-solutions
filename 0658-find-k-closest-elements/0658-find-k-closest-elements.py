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
            if (abs(arr[L] - x) <= abs(arr[R] - x)):
                R -= 1
            else:
                L += 1
        return arr[L:R + 1]

