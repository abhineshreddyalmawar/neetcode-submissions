class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=["+", "-", "/", "*"]
        for token in tokens:
            if token in operators:
                b=stack.pop()
                a=stack.pop()
                if token =="+":
                    result = a+b
                elif token =="-":
                    result = a-b
                elif token == "*":
                    result = a*b
                elif token =="/":
                    result = int(a/b)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]
print(Solution().evalRPN(["1","2","+","3","*","4","-"]))






