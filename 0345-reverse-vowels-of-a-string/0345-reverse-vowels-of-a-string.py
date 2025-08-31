class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        L = 0
        R = len(s) - 1

        vowels = "aeiouAEIOU"
        while L < R:
            while L < R and s[L] not in vowels:
                L += 1
            while L < R and s[R] not in vowels:
                R -= 1
            s[R], s[L] = s[L], s[R]
            L += 1
            R -= 1
        return ''.join(s)