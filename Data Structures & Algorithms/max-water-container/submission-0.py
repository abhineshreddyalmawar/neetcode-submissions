class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0 #initializing left pointer as zero to start with to hold water as pair with right
        right=len(heights)-1 #initializing right pointer as 7 to start with to hold water as pair with left
        best=0 # best is result of max water that it can hold and initialized with zero for now
        while left<right: # 0<7,....
            width=right-left #7-0=7,...
            level= min(heights[left], heights[right])#min(1,6)=1,..
            water = level*width #1*7=7
            if water>best: # 7>0
                best=water # best =7
            if heights[left]<heights[right]:#1<6
                left = left+1 #left =0+1=1,
            elif heights[left]>heights[right]:#skip
                right =right-1#skip
            else:#skip
                left = left+1 #skip
        return best
print(Solution().maxArea([1,7,2,5,4,7,3,6]))