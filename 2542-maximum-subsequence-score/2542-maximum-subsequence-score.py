import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        tuples = list(zip(nums1, nums2))
        tuples.sort(key=lambda tup: tup[1], reverse=True) # sort based on nums2

        res = 0
        n1heap = list() # currently chosen values in nums1
        n1sum = 0

        # n2 is always the current min value of chosen values in nums2, because of the sorting
        for n1, n2 in tuples:
            heapq.heappush(n1heap, n1)
            n1sum += n1
            if len(n1heap) > k:
                n1sum -= heapq.heappop(n1heap)
            if len(n1heap) == k:
                res = max(res, n1sum * n2)
        return res