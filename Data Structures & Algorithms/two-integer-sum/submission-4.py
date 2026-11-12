class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i, value in enumerate(nums):
            diff = target - value

            if diff in m:
                return [m[diff], i]

            m[value] = i

            
        return []
        