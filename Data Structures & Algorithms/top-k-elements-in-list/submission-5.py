class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        build={}
        for num in nums: # for 1,2,2,3,3,3, in nums, 
            if num in build: # if 1,2,2,3,3,3 in build
                build[num]=build[num]+1 # executes by adding +1 for num = 2,3,3 when it exists already in build
            else:
                build[num]=1 #executes for num =1,2,3 when not exists in build
        ordered = sorted(build.items(), key=lambda pair:pair[1], reverse=True) # builds the ordered key, values pair for dict build in descending order [(3,3), (2,2), (1,1)]
        result=[]
        for pair in ordered[:k]: # for every pair in ordered [(3,3), (2,2)]
            result.append(pair[0]) # result=[3,2]
        return result
print(Solution().topKFrequent([1,2,2,3,3,3], 2))
print(Solution().topKFrequent([7,7], 1))

