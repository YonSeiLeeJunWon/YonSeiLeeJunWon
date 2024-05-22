Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        total=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                total+=i
                if i!=num//i:
                    total+=num//i
        if num==1:
            return False
        else:
            return total==num
        
