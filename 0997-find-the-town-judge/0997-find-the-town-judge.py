class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1

        trustedByCounter = Counter()
        trustsSomeone = set()
        for (a, b) in trust:
            trustsSomeone.add(a)
            trustedByCounter[b] += 1
        
        trustedByAll = [key for key, count in trustedByCounter.items() if count == n - 1]

        for a in trustedByAll:
            if a not in trustsSomeone:
                return a
        
        return -1