class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set() # set for have i seen before=(zxy),(x)
        best=0 # best running number for length =3, 1
        left=0 # initialzing pointer for left =0
        for right in range(len(s)):#for right=0,1,2,3,4,5,6
            while s[right] in seen: # while 0,1,2:z,x,y in seen:no;3,4,5,6:z,x,y,z
                seen.remove(s[left]) #skip for 0,1,2:z,x,y;remove:z,x,y,z
                left = left+1 #skip for 0,1,2:z,x,y;left=1,2,3,4
            seen.add(s[right]) # add to set z,x,y,z,x,y,z
            length =right-left+1 # 0-0+1:1,1-0+1:2,2-0+1:3,3-1+1:3,4-2+1:3,5-3+1:3
            if length>best:#1>0,2>0,3>0
                best=length#best=1,2,3
        return best
print(Solution().lengthOfLongestSubstring("zxyzxyz"))
print(Solution().lengthOfLongestSubstring("xxxx"))
        