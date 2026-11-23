class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for position, speed in cars:
            hours = (target - position)/speed
            if stack==[] or hours>stack[-1]:
                stack.append(hours)
        return len(stack)
print(Solution().carFleet(target = 10, position = [1,4], speed = [3,2]))
print(Solution().carFleet(target = 10, position = [4,1,0,7], speed = [2,2,1,1]))

        