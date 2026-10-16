class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_members = []
        for num in nums:
            if unique_members.count(num) > 0:
                return True
            else:
                unique_members.append(num)
        return False