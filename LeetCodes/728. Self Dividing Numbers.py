Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        count=0
        Lst=[]
        for num in range(left,right+1):
            for digit in str(num):
                if int(digit)!=0 and num%int(digit)==0:
                    count+=1
            if count==len(str(num)):
                Lst.append(num)
            count=0
        return Lst
    
