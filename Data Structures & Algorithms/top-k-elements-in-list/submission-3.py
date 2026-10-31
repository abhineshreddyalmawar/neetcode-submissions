class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        build={}
        for num in nums:
            if num in build:
                build[num]=build[num]+1
            else:
                build[num]=1
        ordered = sorted(build.items(), key=lambda pair:pair[1], reverse=True)
        result=[]
        for pair in ordered[:k]:
            result.append(pair[0])
        return result
print(Solution().topKFrequent([1,2,2,3,3,3], 2))
print(Solution().topKFrequent([7,7], 1))

