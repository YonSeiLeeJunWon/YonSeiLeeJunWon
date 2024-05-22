class Solution:
    def countEven(self, num: int) -> int:
        count=0
        for i in range(1,num+1):
            total=0
            lst=[]
            for digit in str(i):
                lst.append(digit)
            for k in lst:
                total=total+int(k)
            if total%2==0:
                count+=1 
        return count
    
