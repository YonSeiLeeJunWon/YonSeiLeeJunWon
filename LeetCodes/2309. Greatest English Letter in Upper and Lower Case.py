class Solution:
    def greatestLetter(self, s: str) -> str:
        result = " "
        for i in s:
            for j in s:
                if i == i.lower() and j == i.upper() and ord(j) >= ord(result):
                    result=j
        if result==" ":
            return ""
        else:
            return result
        
