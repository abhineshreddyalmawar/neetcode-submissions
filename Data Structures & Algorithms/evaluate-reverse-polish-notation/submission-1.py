class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[] # initialized the stack clean
        operators=["+", "-", "*", "/"] # defined list of operators 
        for token in tokens: # for "1","2","+","3","*","4","-" in string
            if token in operators:#if is true for +,-,*
                b=stack.pop() #if +:stack[-1]:pop 2; now stack=[3, 3] if*:stack[-1]:pop 3, now stack:[9,4] if-:stack[-1]:pop 4
                a=stack.pop() #if +:stack[-2]:1; if *: stack[-2]:3; stack[-2]:pop 9
                if token == "+":#if is true for +
                    result=a+b # 1+2:3
                elif token=="-":# if-:true
                    result = a-b # 9-4:5
                elif token =="/":
                    result = int(a/b)
                elif token =="*": # if:* then 3*3:9
                    result = a*b
                stack.append(result) #appends 3 to stack for +;appends 9 to stack for *;appends 5 to stack for *;
            else: 
                stack.append(int(token))#appends:stack=[1, 2] initially, second stack[3, 3]
        return stack[-1] # returns 5 from stack[-1]:stack=[5]
print(Solution().evalRPN(["1","2","+","3","*","4","-"]))