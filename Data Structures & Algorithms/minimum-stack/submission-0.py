class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[1]

    def getMin(self) -> int:
        stackMin = float("infinity")
        for i in self.stack:
            stackMin = min(stackMin, i)
        return stackMin
