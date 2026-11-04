class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        groups=[]
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right=len(nums)-1 
            while left<right:
                total = nums[i]+nums[left]+nums[right]
                if total>0:
                    right = right -1
                elif total<0:
                    left = left +1
                else:
                    groups.append([nums[i], nums[left], nums[right]])
                    left = left +1
                    while left<right and nums[left]==nums[left-1]:
                        left=left+1
        return groups
print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([0,1,1]))
print(Solution().threeSum([0,0,0]))
