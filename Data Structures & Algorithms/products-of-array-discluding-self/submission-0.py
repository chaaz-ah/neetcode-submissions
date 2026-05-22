class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        otp = []
        for i in range(len(nums)): 
            mul = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                mul *= nums[j]
            otp.append(mul)
        return otp

        #lwk kinda got the concept but kinda chatgpt helped me out