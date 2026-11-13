class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts={}
        best =0
        left=0
        for right in range(len(s)):
            if s[right] in counts:
                counts[s[right]]=counts[s[right]]+1
            else:
                counts[s[right]]=1
            while ((right-left+1)-max(counts.values()))>k:
                counts[s[left]]=counts[s[left]]-1
                left = left+1
            length =right-left+1
            if length>best:
                best = length
        return best
print(Solution().characterReplacement("XYYX", 2))
print(Solution().characterReplacement("AAABABB", 1))





        

        