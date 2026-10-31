class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            partner = target - nums[i]
            if partner in seen:
                return [seen[partner], i]
            else:
                seen[nums[i]]=i
print(Solution().twoSum([3,4,5,6], 7))
print(Solution().twoSum([4,5,6], 10))
print(Solution().twoSum([5,5], 10))