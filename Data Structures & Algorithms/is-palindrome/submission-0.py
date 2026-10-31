class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned =[]
        for char in s:
            if char .isalnum():
                cleaned.append(char.lower())
        left =0
        right = len(cleaned)-1
        while left<right:
            if cleaned[left]!=cleaned[right]:
                return False
            left=left+1
            right=right-1    
        return True    
            
print(Solution().isPalindrome("Was it a car or a cat I saw?"))
print(Solution().isPalindrome("tab a cat"))
