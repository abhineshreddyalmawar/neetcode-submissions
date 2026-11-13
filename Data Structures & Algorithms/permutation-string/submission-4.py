class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts={}
        for char in s1:
            if char in s1_counts:
                s1_counts[char]=s1_counts[char]+1
            else:
                s1_counts[char]=1
        counts={}
        left=0
        for right in range(len(s2)):
            if s2[right] in counts:
                counts[s2[right]]=counts[s2[right]]+1
            else:
                counts[s2[right]]=1
            while (right-left+1)>len(s1):
                    counts[s2[left]]=counts[s2[left]]-1
                    if counts[s2[left]]==0:
                        del counts[s2[left]]
                    left=left+1    
            if s1_counts==counts:
                return True
        return False    
print(Solution().checkInclusion(s1 = "abc", s2 = "lecabee"))
print(Solution().checkInclusion(s1 = "abc", s2 = "lecaabee"))





        
                        