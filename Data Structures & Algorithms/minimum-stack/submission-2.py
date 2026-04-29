class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        top = self.stack [-1]
        return top

    def getMin(self) -> int:
        res = 10000000000
        for i in range(len(self.stack)): 
            res = min(self.stack[i], res)
        return res