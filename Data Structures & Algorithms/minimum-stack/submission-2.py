class MinStack:

    def __init__(self):
        self.stack = []
        self.stackMin = []

    def push(self, val: int) -> None:
        if self.stackMin:
            self.stackMin.append(min(val, self.stackMin[-1]))
        else:
            self.stackMin.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stackMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackMin[-1]
