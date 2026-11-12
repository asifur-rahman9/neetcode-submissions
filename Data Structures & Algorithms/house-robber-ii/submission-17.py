class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            return max(self.solve(nums[1:], n),self.solve(nums[:-1], n))
        
   
    def solve(self, nums, n):

        rob1 = 0
        rob2 = 0
        current = 0

        for i in nums:
            print(i)
            current = max(rob1 + i, rob2)
            rob1 = rob2
            rob2 = current

        return rob2

