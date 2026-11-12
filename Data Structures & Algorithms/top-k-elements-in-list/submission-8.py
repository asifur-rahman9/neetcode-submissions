from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        m = Counter(nums)
        l = []
        sort_items = sorted(m.items(), key=lambda items:items[1], reverse = True)

        for i in range(k):
            l.append(sort_items[i][0])

        
        return l
                

        
        