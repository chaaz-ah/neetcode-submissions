class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        output = []
        for i in range(len(nums)):
            mul = 1
            mul *= nums[i]
            prefix.append(mul)
        for i in range(len(nums)-1, 0, -1):
            mul = 1
            mul *= nums[i]
            postfix.append(mul)
        for i in range(len(nums)):
            mul = 1
            if i != 0 | i != len(nums)-1:
                mul = prefix[i-1] * postfix[i+1]
            output.append(mul)

        return output
        #this is what i derived without solution lol but watched neetcode vid for the first thing js to see algorithmic explanation