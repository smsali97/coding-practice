class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.MIN_SO_FAR = None
        

    def push(self, x: int) -> None:
        if self.MIN_SO_FAR is not None and self.getMin() is not None:
            self.MIN_SO_FAR = min(x,self.getMin())
        else:
            self.MIN_SO_FAR = x
        
        self.stack.append((x,self.MIN_SO_FAR))
        
        print(self.stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        if len(self.stack) >= 1:
            val, vmin = self.stack[-1]
            return val

    def getMin(self) -> int:
        if len(self.stack) >= 1:
            val, vmin = self.stack[-1]
            return vmin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()