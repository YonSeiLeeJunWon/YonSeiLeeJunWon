class Solution:
    def scoreOfString(self, s: str) -> int:
        total=0
        for i in range(0,len(s)-1):
            total=total+abs(ord(s[i+1])-ord(s[i]))
        return total
    
