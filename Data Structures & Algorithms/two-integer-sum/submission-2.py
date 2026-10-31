class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i in range(len(nums)): # for i in range(3) which starts with position 0, then 1
            partner = target - nums[i] # partner for i =0 is 4, for i=1 is 3
            if partner in seen: # if 4 in seen, if 3 in seen
                return[seen[partner], i] #skip for if 4 in seen, if 3 in seen executes and returns the pair[0, 1]
            else:
                seen[nums[i]]=i # execute for 4 in seen being not exists seen[4]=0 is updated to dict={4:0}

print(Solution().twoSum([3,4,5,6], 7))
print(Solution().twoSum([4,5,6], 10))
