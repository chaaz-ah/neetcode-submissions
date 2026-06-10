class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i:
                    res = max((prices[j] - prices[i]), res)
        return res
        #got the brute force ig 