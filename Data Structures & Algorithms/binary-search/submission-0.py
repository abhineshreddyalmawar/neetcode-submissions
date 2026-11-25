class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0 # initializing left =0
        right = (len(nums)-1) # right = 5
        while left<=right:#0<=5:yes,3<=5:yes,3<=3:yes
            middle = (left+right)//2 #middle:2,4,3
            if nums[middle] == target:# 2==4:no;6==4:no,4=4:yes
                return middle #4==4 return 3
            elif nums[middle]<target:#2<4:yes;6<4:no
                left = middle +1#middle=2:left=3
            else:#6<4:yes
                right = middle -1#middle=4;right=3
        return -1
print(Solution().search([-1,0,2,4,6,8], 4))
print(Solution().search([-1,0,2,4,6,8], 3))
        