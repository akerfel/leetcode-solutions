class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        L = 0
        target = collections.Counter(s1)
        window = dict()
        for R in range(len(s2)):
            window[s2[R]] = window.get(s2[R], 0) + 1
            if (R - L >= len(s1)):
                window[s2[L]] -= 1
                if (window[s2[L]] == 0):
                    window.pop(s2[L])
                L += 1
            if (window == target):
                return True
        return False