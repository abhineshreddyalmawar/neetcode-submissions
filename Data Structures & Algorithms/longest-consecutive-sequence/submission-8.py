class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        build = set(nums) # building set here being we want to no -1,+1 exists in it with o(1)
        best = 0 # defining best and initializing as zero being we need the final result as number which is count of consecutive numbers
        for number in nums: # looping thru every number in list of nums 2,20,4,10,3,4,5
            behind = number-1  # for (2,20,4,10,3,4,5) - 1;
            if behind not in build: # True for if behind=1,19,9 being not in build
                current = number #executes when if true sets current = 2,20,10
                length = 1 # executes when if true, length =1 fo all
                while current+1 in build:# True for while 2+1,3+1,4+1,5+1
                    current = current+1 #current=3,4,5
                    length = length+1 #length =2,3,4
                if length>best: # 4>0
                    best=length #best =4
        return best # returns 4

print(Solution().longestConsecutive([2,20,4,10,3,4,5]))
print(Solution().longestConsecutive([0,3,2,5,4,6,1,1]))