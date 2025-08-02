class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        R = len(nums) - 1
        res = 0
        mod = 10**9 + 7

        for L in range(len(nums)):
            while nums[L] + nums[R] > target and L <= R:
                R -= 1
            if L <= R:
                res += 2**(R-L)
                res %= mod
        
        return res