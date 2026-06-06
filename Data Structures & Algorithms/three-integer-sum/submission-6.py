class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i -1]:
                continue
            #also dont get lines 6-7
            s = i + 1
            e = len(nums)-1

            while s < e:
                twoSum = nums[s] + nums[e] + a

                if twoSum > 0:
                    e -= 1
                elif twoSum < 0:
                    s += 1
                else:
                    result.append([a, nums[s], nums[e]])
                    #i dont get why we do the following like lines21-24 for
                    s += 1
                    e -= 1
                    while nums[s] == nums[s-1] and s < e:
                        s += 1
        return result
                 

