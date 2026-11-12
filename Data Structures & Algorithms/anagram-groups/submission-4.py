class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        l = []

        for s in strs:
            m["".join(sorted(s))].append(s)

        for value in m.values():
            l.append(value)
        return l
