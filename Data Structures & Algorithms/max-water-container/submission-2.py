class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        best=0
        while left<right:
            width = right - left
            level = min(heights[left], heights[right])
            water=level * width
            if water > best:
                best=water
            if heights[left]<heights[right]:
                left=left+1
            elif heights[left]>heights[right]:
                right = right-1
            else:
                left=left+1
        return best
print(Solution().maxArea([1,7,2,5,4,7,3,6]))
print(Solution().maxArea([2,2,2]))


