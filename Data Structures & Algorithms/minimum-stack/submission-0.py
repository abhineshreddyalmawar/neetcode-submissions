class MinStack:
    def __init__(self):
        self.stack=[]

    def push(self, val: int) ->None:
        if self.stack==[]:
            smallest_so_far=val
        else:
            smallest_so_far=min(val, self.stack[-1][1])
        self.stack.append([val, smallest_so_far])

    def pop(self)->None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) ->int:
        return self.stack[-1][1]

obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(0)
print(obj.getMin())   # 0
obj.pop()
print(obj.top())      # 2
print(obj.getMin())   # 1
        
