class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned =[] # creating cleaned list for cleaning the string
        for char in s: #lopping thru "Was it a car or a cat I saw?"
            if char .isalnum(): # passes for alphabets and numeric, rest skipped
                cleaned.append(char.lower()) # appends all alphabets/numeric in lowercase
        left = 0 # initialzing the pointer as zero to start very first position of cleaned
        right = len(cleaned)-1 #initializing the right pointer from right last position 18
        while left<right: # keep going while left before is right
            if cleaned[left]!=cleaned[right]: # checks whether the chars match initially
                return False # returns false if passes the above
            left = left +1 #if not passes then it continues by +1 of the pointer position 
            right = right -1 #if not passes then it continues by -1 of the pointer position
        return True # once loop exits return result
print(Solution().isPalindrome("Was it a car or a cat I saw?"))
print(Solution().isPalindrome("tab a cat"))


        

