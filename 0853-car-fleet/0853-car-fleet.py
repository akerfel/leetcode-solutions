class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = deque()
        stack.append(cars[0])
        for car in cars[1:]:
            if not self.catchesUp(car, stack[-1], target):
                stack.append(car)

        return len(stack)

    def catchesUp(self, behind, ahead, target):
        # v = s / t => t = s / v
        behindArriveTime = (target - behind[0]) / behind[1]
        aheadArriveTime = (target - ahead[0]) / ahead[1]
        return behindArriveTime <= aheadArriveTime