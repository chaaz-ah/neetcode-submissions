class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highArea = 0
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                area = (min(heights[i], heights[j])) * (j-i)
                if area > highArea:
                    highArea = area
        return highArea
    #did this on my own lol