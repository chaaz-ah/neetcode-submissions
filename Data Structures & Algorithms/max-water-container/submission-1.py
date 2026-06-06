class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s = 0
        e = len(heights)-1
        minArea = 0
        while s < e:
            if min(heights[s], heights[e]) * (s-e) > minArea:
                minArea = min(heights[s], heights[e]) * (s-e)
            else:
                if heights[s] > heights[e]:
                    e -= 1
                if heights[s] < heights[e]:
                    s += 1
        return minArea
        #alr this is what i thought of ig

            
