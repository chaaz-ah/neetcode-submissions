class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s = 0
        e = len(heights)-1
        minArea = 0
        while s < e:
            area = min(heights[s], heights[e]) * (e-s)
            minArea = max(area, minArea)

            if heights[s] > heights[e]:
                e -= 1
            elif heights[s] < heights[e]:
                s += 1
            else: 
                e -= 1
            
        return minArea
        #broooo omg i almost got it i did s-e instead of e-s but kinda saw some hints and vid and also the hint that you should move the larger height was monumental

            
