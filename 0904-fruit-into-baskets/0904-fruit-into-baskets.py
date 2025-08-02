from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = Counter()
        L = 0
        res = 0
        
        for R in range(len(fruits)):
            counter[fruits[R]] += 1
            
            # drop fruits until carrying two fruit types
            while len(counter) > 2:
                counter[fruits[L]] -= 1
                if counter[fruits[L]] == 0:
                    counter.pop(fruits[L])
                L += 1
            
            res = max(res, R - L + 1)
        
        return res