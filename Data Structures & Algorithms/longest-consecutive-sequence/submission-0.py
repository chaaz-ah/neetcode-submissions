class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
            else:
                continue
        count += 1
        return count