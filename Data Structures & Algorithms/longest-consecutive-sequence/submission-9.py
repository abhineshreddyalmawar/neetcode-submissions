class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        build = set(nums)
        best = 0
        for number in nums:
            key = number -1
            if key not in build:
                current = number
                length =1
                while current +1 in build:
                    current = current +1
                    length = length +1
                if length>best:
                    best = length
        return best
print(Solution().longestConsecutive([2,20,4,10,3,4,5]))
print(Solution().longestConsecutive([0,3,2,5,4,6,1,1]))