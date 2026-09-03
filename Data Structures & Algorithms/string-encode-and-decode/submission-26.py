class Solution:

    def encode(self, strs: List[str]) -> str:
        s = str(len(strs)) + '++'
        for i in strs:
            s = s + str(len(i)) + '+' + i + '++'
        return s[0:len(s)-2]

    def decode(self, s: str) -> List[str]:
        list1 = []
        k = 0
        while k < len(s) and s[k] != '+':   # bounds-checked now
            k += 1
        len1 = int(s[0:k])
        if len1 == 0:
            return list1                     # nothing more to parse
        i = k
        while len1 > 0:
            if s[i] == '+' and s[i+1] == '+':
                j = i + 2
                while s[j] != '+':
                    j += 1
                len2 = int(s[i+2:j])
                list1.append(s[j+1:j+1+len2])
                i = j + 1 + len2
                len1 -= 1
        return list1