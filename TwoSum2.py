class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # use hashmap to reduce O to O(n)

        seen_nums = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen_nums:
                return [seen_nums[need], i]
            seen_nums[num] = i
        return []