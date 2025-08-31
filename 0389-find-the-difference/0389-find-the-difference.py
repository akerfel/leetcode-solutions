class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count1 = Counter(s)
        count2 = Counter(t)

        #print(count1)
        for c, num1 in count1.items():
            print(c)
            print(num1)
            num2 = count2[c]
            if (num1 != num2):
                return c
            count2[c] = -1 # marked as "not the one"

        # the added letter is not present at all in s
        for c, num in count2.items():
            if num != -1:
                return c