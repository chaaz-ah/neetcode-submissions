class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = defaultdict()
        for ind, num in enumerate(position):
            pair[num] = speed[ind]
        pair = dict(sorted(pair.items(), reverse=True)) #dont know this concept really

        stack = []
        for p, s in pair.items(): #dont understand when to use .items()
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


        

