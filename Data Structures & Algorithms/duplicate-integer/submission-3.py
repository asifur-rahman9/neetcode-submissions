class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = defaultdict(int)

        for i in nums:
            dup[i] += 1 
        print(dup)

        for i in dup.keys():
            print(i)
            if dup.get(i, 0) != 1:
                print(dup.get(i, 0))
                return True
        
        return False
