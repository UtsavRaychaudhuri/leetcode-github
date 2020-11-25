class MinStack:
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.my_stack=collections.deque([])
        
​
    def push(self, x: int) -> None:
        if len(self.my_stack)==0:
            self.my_stack.append([x,x])
        else:
            min_element=min(x,self.my_stack[-1][1])
            self.my_stack.append([x,min_element])
            
​
    def pop(self) -> None:
        self.my_stack.pop()
        
​
    def top(self) -> int:
        return self.my_stack[-1][0]
        
​
    def getMin(self) -> int:
        return self.my_stack[-1][1]
        
​
​
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
