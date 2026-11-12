'''
if anagram -> true
else -> false
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dup = defaultdict(int)
        for i in s:
            dup[i] +=1
        for i in t:
            dup[i] -=1
        
        for i in dup.values():
            if i != 0:
                return False

        return True
            
            

        