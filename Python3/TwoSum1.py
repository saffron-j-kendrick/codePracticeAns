class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for i in range(len(nums)):
            if i == len(nums):
                    break
            for j in range(1, len(nums)):
                if j == len(nums):
                    break
                if j == i:
                    j +=1
                if nums[i] + nums[j] == target:
                    return [i, j]
                else:
                    j+=1
            i +=1


# has order O(n^2)

