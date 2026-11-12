class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = defaultdict(int)

        for i in nums:
            dup[i] += 1 
        print(dup)

        for i in dup.keys():
            if dup.get(i) != 1:
                return True
        
        return False
