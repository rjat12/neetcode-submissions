from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d= defaultdict(list)
        for i in strs:
            v = ''.join(sorted(i))
            d[v].append(i)
        arr1=[]
        for key,values in d.items():
            arr1.append(values)
        return arr1

        