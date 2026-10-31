class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): # len(jar)=len(jam)
            return False # skip
        count_s={}
        count_t={}

        for char in s: # for j, a, r
            if char in count_s: # if j in count_s, if a in count_s, if r in count_s
                count_s[char]=count_s[char]+1 #skips
            else:
                count_s[char]=1 # # executes count_s={j:1, a:1, r:1}
        for char in t: # for j, a, m
            if char in count_t: # if j in count_t, if a in count_t, if r in count_t
                count_t[char]=count_t[char]+1 #skips
            else:
                count_t[char]=1 # executes count_t={j:1, a:1, m:1}
        return(count_s==count_t) # count_s={j:1, a:1, r:1} != count_t={j:1, a:1, m:1}
print(Solution().isAnagram("s=racecar", t="carrace"))
print(Solution().isAnagram("s=jar", t="jam"))
    
    




