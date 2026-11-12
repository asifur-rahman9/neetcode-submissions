class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if n == 1 and not trust:
            return 1
        
        dic = {}
        trusts_one = set()

        for u, v in trust:
            trusts_one.add(u)
            if v not in dic:
                dic[v] = [u]

            else:
                dic[v].append(u)

        for judge in dic:
            if len(dic[judge]) == n-1 and judge not in trusts_one:
                return judge
        
        return -1
                

            
