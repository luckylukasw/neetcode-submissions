class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_members = []
        for num in nums:
            if num in unique_members:
                return True
            else:
                unique_members.append(num)
        return False