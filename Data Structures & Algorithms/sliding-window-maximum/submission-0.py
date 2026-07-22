class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        maxNum = 0
        res = []

        for r in range(k-1, len(nums)):
            maxNum = 0
            for i in range(l, r+1):
                maxNum = max(nums[i], maxNum)

            res.append(maxNum)
            l += 1
        
        return res

#BROOOOOOO I ACTUALLY DID THIS BY MYSELF NO SHOT THIS IS LEETCODE HARD BUT I HAD TO DEBUG A LIL 