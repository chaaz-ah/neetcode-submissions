class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        result.add(tuple([nums[i], nums[j], nums[k]]))
        result = list(result)
        return result #bruh looked solution a little also forgot like set vs list like the append vs add bruh
                        
