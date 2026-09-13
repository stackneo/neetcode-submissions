class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if self.minStack:
            lowest_cur_val = self.minStack[-1]
            if val < lowest_cur_val:
                self.minStack.append(val)
            else:
                self.minStack.append(lowest_cur_val)
        else:
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
