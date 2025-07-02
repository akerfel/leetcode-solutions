class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = list() # tuple(index, temp)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                pop = stack.pop()
                res[pop[0]] = i - pop[0]
            stack.append((i, t))
        
        return res