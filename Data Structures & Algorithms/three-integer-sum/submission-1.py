class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)-2):
            s = i+1
            e = len(nums)-1
            
            while s < e:
                partial_sum = nums[s] + nums[e]
            
                if partial_sum + i > 0:
                    e -= 1
                elif partial_sum + i < 0:
                    s += 1
                else:
                    return [[nums[i], nums[s], nums[e]]]
            
        return [[]] #bruh idk lwk forgot ts wasnt sorted 