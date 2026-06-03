class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        e = len(numbers)-1

        while s < e:
            if numbers[s] + numbers[e] > target:
                e -= 1
            if numbers[s] + numbers[e] < target:
                s += 1
            if numbers[s] + numbers[e] == target:
                return [s+1, e+1]
        return []

        #omg i saw the neetcode video on the process but i implemented this by myself prob not too like amazing or idk
                