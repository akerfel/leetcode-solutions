class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        P = 0   # points to positive num
        N = 0   # points to negative num
        res = list()
        addPos = True
        n = len(nums)
        while len(res) < n:
            if addPos:
                while P < n and nums[P] < 0:
                    P += 1
                res.append(nums[P])
                P += 1
            else:
                while N < n and nums[N] > 0:
                    N += 1
                res.append(nums[N])
                N += 1
            addPos = not addPos
        
        return res
