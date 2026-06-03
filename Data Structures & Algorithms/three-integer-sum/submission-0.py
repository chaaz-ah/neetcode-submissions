class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        for i, first_num in enumerate(nums):
            s = i+1
            e = len(nums)-1
            
            partial_sum = nums[s] + nums[e]

            if partial_sum + i > 0:
                e -= 1
            elif partial_sum + i < 0:
                s += 1
            else:
                return [nums[i], nums[s], nums[e]]
            
        return [[]]