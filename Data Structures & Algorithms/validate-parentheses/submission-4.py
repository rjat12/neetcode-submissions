class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for i in s:
            if (i == '(' or i == '{' or i == '['):
                arr.append(i)
                print(arr)
            else:
                if len(arr)==0:
                    return False
                else:
                    if (arr[-1] == '(' and i ==')'):
                        arr.pop()
                    elif (arr[-1] == '[' and i ==']'):
                        arr.pop()
                    elif (arr[-1] == '{' and i =='}'):
                        arr.pop()
                    else:
                        return False
        if len(arr)>=1:
            return False
        return True

        