class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if (nums[i] + nums[j] + nums[k] == 0) and ((nums[i] != nums[j]) and (nums[j] != nums[k]) and (nums[i] != nums[k])):
                        s = [nums[i], nums[j], nums[k]]
                        s.sort()
                        if s not in result:
                            result.append(s)
        return result #bruh why doesnt this work
                        
