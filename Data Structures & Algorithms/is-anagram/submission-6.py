class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        counts_s={}
        counts_t={}

        for char in s:
            if char in counts_s:
                counts_s[char]=counts_s[char]+1
            else:
                counts_s[char]=1
        
        for char in t:
            if char in counts_t:
                counts_t[char]=counts_t[char]+1
            else:
                counts_t[char]=1
        
        return(counts_s==counts_t)

print(Solution().isAnagram(s = "racecar", t = "carrace"))
print(Solution().isAnagram(s = "jar", t = "jam"))
    
    




