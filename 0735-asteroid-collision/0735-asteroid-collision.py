class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = list()
        for a in asteroids:
            if a < 0:
                # let it destroy all smaller positive asteroids
                while stack and stack[-1] > 0 and stack[-1] < abs(a):
                    stack.pop()

                if not stack or stack[-1] < 0:
                    stack.append(a)
                elif stack[-1] == abs(a):
                    stack.pop()
            else:
                stack.append(a)
        return stack
        