class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        L = 0
        R = len(numbers) - 1

        while (R > L):
            if (numbers[L] + numbers[R] == target):
                return [L + 1, R + 1]
            if (numbers[L] + numbers[R] > target):
                R -= 1
            else:
                L += 1