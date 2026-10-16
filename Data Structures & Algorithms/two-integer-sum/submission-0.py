class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_set = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] not in complement_set:
                complement_set[complement] = i
            else:
                return [complement_set[nums[i]], i]