class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]*len(nums) # define result as list mutliplied by one to hold the same value calculate from product
        left=1 # initialize as 1 being for  i=0 left product is nothing and when multiplied it is not zero
        for i in range(len(nums)):# loop thru i=0,1,2,3
            result[i]=left # define result[i] =1 initially =[1,1,2,8]
            left=left*nums[i] #calculate left product left = 1*0,1*1,1*2,2*4
        
        right=1 # initialize as 1 being for  i=0 right product is nothing and when multiplied it is not zero
        for i in range(len(nums)-1,-1,-1): # loop thru i=3,2,1,0
            result[i]=result[i]*right # left*right product:8*1,2*6,1*24,1*48
            right=right*nums[i] #  right=1*0,1*6,6*4,24*2
        return result

print(Solution().productExceptSelf([1,2,4,6]))
print(Solution().productExceptSelf([-1,0,1,2,3]))

           