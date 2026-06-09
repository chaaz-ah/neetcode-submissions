class Solution:
    def trap(self, height: List[int]) -> int:
        s = 0
        while height[s] != 0:
            s += 1
        maxWater = 0
        for i in range(1, len(height)-1):
            l = i-1
            r = i+1

            water = min(height[l], height[r]) - height[i]
            maxWater = max(water, maxWater)

        return maxWater
        #bruh idk

