class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = L + ((R - L) // 2)

            if target > nums[mid]:
                L = mid + 1
            elif target < nums[mid]:
                R = mid - 1
            else:
                return mid
        return -1