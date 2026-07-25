class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numList = []
        for i in tokens:
            if i.isnumeric():
                numList.append(i)
            else:
                j = numList.pop()
                k = numList.pop()
                if i == "+":
                    out += k + j
                if i == "*":
                    out *= j * k
                if i == "/":
                    out /= k / j

                    #bruh idk
                

