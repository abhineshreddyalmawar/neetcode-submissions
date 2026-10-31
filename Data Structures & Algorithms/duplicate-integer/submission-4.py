class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums: # 1 in nums, 2 in nums, 3 in nums, 3 in nums
            if num in seen: # 1 in seen, 2 in seen, 3 in seen, 3 in seen
               return True # skips for 1,2,3 and returns true for last position 3
            else:
                seen.add(num) # adds for 1,2,3
        return False # returns false if nothing is returned true
print(Solution().hasDuplicate([1, 2, 3, 3]))
print(Solution().hasDuplicate([1, 2, 3, 4]))