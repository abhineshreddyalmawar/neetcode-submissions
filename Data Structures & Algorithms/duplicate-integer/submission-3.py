class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
               return True
            else:
                seen.add(num)
        return False
print(Solution().hasDuplicate([1, 2, 3, 3]))