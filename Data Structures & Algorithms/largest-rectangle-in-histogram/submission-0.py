class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        stack = []
        for i, val in enumerate(heights):
            if stack and stack[-1][1] > val:
                stack.append([stack[-1], val])
                maxArea = max(maxArea, (stack[-2][1] * stack[-2][0]))
                stack.pop()
            else:
                stack.append([i, val])
        return maxArea

        #i got some like this frmo video