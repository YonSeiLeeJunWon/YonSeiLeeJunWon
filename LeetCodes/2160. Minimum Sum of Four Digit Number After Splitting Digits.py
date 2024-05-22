Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def minimumSum(self, num: int) -> int:
...         digits = [int(d) for d in str(num)] 
...         
...         digits.sort()
...         
...         new1=0
...         new2=0
...         for i in range(len(digits)):
...             if i%2==0:
...                 new1=new1*10+digits[i]
...             else:
...                 new2=new2*10+digits[i]
...         
...         return new1+new2
