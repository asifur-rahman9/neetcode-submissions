class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmax, curmin = 1,1

        for num in nums:
            if num == 0:
                curmax, curmin = 1,1
                continue

            temp = curmax * num
            curmax = max(num, temp, curmin*num)
            curmin = min(num, temp, curmin*num)
            res = max(curmax, res)

        return res
        