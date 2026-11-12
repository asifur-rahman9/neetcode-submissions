class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set(nums)

        if len(nums) != len(dup):
            return True
        else:
            return False

