class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        otp = [0] * len(nums)
        for i in range(len(nums)): 
            mul = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                mul *= nums[j]
            otp[i] = mul
        return otp