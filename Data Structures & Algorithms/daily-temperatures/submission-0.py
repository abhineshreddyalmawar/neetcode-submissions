class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = ([0]*len(temperatures)) # initializing answers for final result with list of zeros qith size equivalent to length of temperatures [0,0,0,0,0,0,0]
        stack = [] # for waiting day temp:[]
        for day in range(len(temperatures)):# for 0,1,2,3
            while stack !=[] and temperatures[day]> temperatures[stack[-1]]:#for 1:38>30:yes;for2:30>38:no;for3:36>30:yes
                a=stack.pop()#for1:a=pop(0);for3:pop(2)
                result = day - a #for1:1-0=1;for3:3-2:1
                answer[a]=result#for1:answer=[1],[1,1]
            stack.append(day)#for1:[0];2:[1],3:[]
        return answer #[1,0,0,0,0,0,0]
print(Solution().dailyTemperatures([30,38,30,36,35,40,28]))
print(Solution().dailyTemperatures([22,21,20]))
        