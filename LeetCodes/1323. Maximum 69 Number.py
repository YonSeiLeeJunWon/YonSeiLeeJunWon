Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def maximum69Number (self, num: int) -> int:
        lst=[]
        for i in str(num):
            lst.append(i)
        for i in range(0,len(lst)):
            if lst[i]=="6":
                lst[i]="9"
                return int(''.join(lst))
        return int(num)
    
