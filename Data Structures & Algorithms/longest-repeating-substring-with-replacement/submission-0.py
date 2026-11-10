class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts={} # dict as nb for storing counts of how many times letter appear
        best=0 #best for returning length of longest substring
        left=0 #initializing pointer left with zero
        for right in range(len(s)):# Right=0,1,2,3
            if s[right] in counts:# if s[0]:X in counts:NO, s[1]:Y,S[2]:Y,S[3]:X
                counts[s[right]]=counts[s[right]]+1#S[2]:{X:1,Y:2},S[3]:{X:2,Y:2}
            else:
                counts[s[right]]=1#s[0]:{X:1},S[1]={X:1,Y:1}
            while ((right-left+1)- max(counts.values()))>k:#2>1,((3-1+1)-2:1:1>1:False
                counts[s[left]]=counts[s[left]]-1#{X:1.Y:2}
                left = left +1 # 0+1:1
            length = right-left+1 # length =0-0+1:1,1-0+1:2,2-0+1:3
            if length>best:#1>0,2>0,3>0
                best=length#best=1,2,3
        return best
print(Solution().characterReplacement("XYYX", 2))
print(Solution().characterReplacement("AAABABB", 1))

        