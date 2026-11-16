class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(":")", "{":"}","[":"]"}
        stack=[]
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if stack==[] or pairs[stack[-1]]!=char:
                    return False
                stack.pop()
        if stack==[]:
            return True
        return False
print(Solution().isValid(s="[]"))
print(Solution().isValid(s="([{}])"))
print(Solution().isValid(s="[(])"))

        