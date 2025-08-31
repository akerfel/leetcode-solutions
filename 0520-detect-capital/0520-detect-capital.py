class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        allCapital = True
        allLower = True

        for c in word:
            if c not in capitals:
                allCapital = False
            else:
                allLower = False

        onlyFirst = word[0] in capitals
        for i in range (1, len(word)):
            c = word[i]
            if c in capitals:
                onlyFirst = False
                break

        return allCapital or allLower or onlyFirst