class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            if L == R and target != nums[L]:
                return -1
            mid = (R + L) // 2
            if nums[mid] == target:
                return mid
            if target <= nums[mid]:
                R = mid
            else:
                L = mid + 1
            
        return -1