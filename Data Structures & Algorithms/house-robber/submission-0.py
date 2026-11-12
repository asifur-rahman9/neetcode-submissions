class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        rob1 = 0
        rob2 = 0

        for i in nums:
            current= max(rob1 + i, rob2)
            rob1 = rob2
            rob2 = current
        return rob2
