class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        dic = {}

        for u, v in trust:
            if v not in dic:
                dic[v] = [u]

            else:
                dic[v].append(u)

        for judge in dic:
            if len(dic[v]) == n-1:
                return v
            else:
                return -1
                

            
