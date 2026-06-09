class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [] * len(height)
        maxRight = [] * len(height)
        minLR = [] * len(height)
        water = [] * len(height)

        left = 0
        for i, value in enumerate(height):
            if value > left:
                left = value
            maxLeft[i] = value
        
        right = 0
        for i in range(len(height), 0, -1):
            if value > right:
                right = value
            maxRight[i] = value

        minLR[i] = min(maxLeft[i], maxRight[i])

        if minLR[i] - height[i] < 0:
            water[i] = 0
        else:
            water[i] = minLR[i] - height[i]

        sum = 0
        for i in water:
            sum += water[i]     

        return sum       
        #watched the video but still idk 