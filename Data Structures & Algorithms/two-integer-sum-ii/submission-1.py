class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0 # initializing the left pointers to match with right being array is already sorted from ascending
        right = len(numbers)-1 #initializing the right pointers to match with left being array is already sorted from ascending
        while left<right: # while 1<4, 1<3, 1<2
            sum = numbers[left]+numbers[right] #sum = 1+4=5, 1+3=4, 1+2=3
            if sum == target: #5==3, 4==2, 3==3
                return[left+1, right+1] # skips for 5===3, 4==3, exeutes for 3==3 with return[1,2]
            elif sum>target: # 5>3,4>3
                right=right -1 #right=4-1=3, next right=3-1=2
            else: 
                left=left+1 # skips:5>3, 4>3
print(Solution().twoSum([1,2,3,4],3))
        