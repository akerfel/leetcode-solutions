class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countRansom = Counter(ransomNote)
        countMag = Counter(magazine)

        for c, count in countRansom.items():
            if c not in countMag.keys():
                return False
            if countMag[c] < count:
                return False
        return True