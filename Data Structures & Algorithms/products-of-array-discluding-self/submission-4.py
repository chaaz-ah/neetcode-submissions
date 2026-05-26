class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        otp = [1] * len(nums)
        for i in range(len(nums)):
            otp[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            otp[i] *= postfix
            postfix *= nums[i]
        return otp