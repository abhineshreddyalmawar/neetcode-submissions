class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        for number in nums:
            if number in counts:
                counts[number]=counts[number]+1
            else:
                counts[number]=1
        ordered= sorted(counts.items(), key=lambda pair:pair[1], reverse=True)
        result=[]
        for pair in ordered[:k]:
            result.append(pair[0])
        return result   
print(Solution().topKFrequent([4,4,4,5,7,7], 2))   
print(Solution().topKFrequent([1,2,2,3,3,3], 2))  
print(Solution().topKFrequent([7, 7], 1))  