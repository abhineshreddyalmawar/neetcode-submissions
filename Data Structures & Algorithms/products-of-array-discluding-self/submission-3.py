class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result= [1] * len(nums)
        left =1
        for i in range(len(nums)):
            result[i]=left
            left= left * nums[i]
        right=1
        for i in range(len(nums)-1,-1,-1):
            result[i]=result[i]*right
            right=right*nums[i]
        return result
print(Solution().productExceptSelf([1,2,4,6]))
print(Solution().productExceptSelf([-1,0,1,2,3]))

           