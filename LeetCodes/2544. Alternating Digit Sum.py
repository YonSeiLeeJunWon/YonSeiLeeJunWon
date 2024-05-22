class Solution:
    def alternateDigitSum(self, n: int) -> int:
        total=0
        lst=[]
        for i in str(n):
            lst.append(i)
        for i in range(0,len(lst)):
            total=total+int(lst[i])*(-1)**(i)
        return total
    
