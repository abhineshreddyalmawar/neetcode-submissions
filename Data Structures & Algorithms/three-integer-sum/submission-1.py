class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sorting nums for pointer to find the right pair that equals zero:[-4,-1,-1,0,1,2]
        groups=[] # defining the groups as list to store the final result of lists with pairs
        for i in range(len(nums)): # for 0:-4,1:-1
            if i!=0 and nums[i]==nums[i-1]:#skips for i==0
                continue #pass:i==0
            left=i+1#initializing the left pointers:i+1:0+1,1+1:2
            right=len(nums)-1#initialzing the right pointers: 6-1:5
            while left<right:#1<5,2<5,3<5,4<5,5<5,2<5,3<5
                total = nums[i]+nums[left]+nums[right]#total=-4-1+2=-3,-4-1+2=-3,-4+0+2=-2,-4+1+2=-1,-1-1+2:0
                if total>0:#-3>0:skip
                    right = right-1
                elif total<0:#-3<0,-3<0,-2<0,-1<0
                    left = left +1#1+1:2,2+1:3,3+1:4,4+1:5
                else: 
                    groups.append([nums[i], nums[left], nums[right]])#[-,-1,2]
                    left=left+1#2+1:3
                    while left<right and nums[left]==nums[left-1]:#3<5 and 0!=-1
                        left=left+1
        return groups
print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([0,1,-1]))
print(Solution().threeSum([0,0,0]))