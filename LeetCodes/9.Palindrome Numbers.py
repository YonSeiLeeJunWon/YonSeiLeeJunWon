Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def isPalindrome(self, x: int) -> bool:
...         count=0
...         x=str(x)
...         a=1
...         for i in x:
...             if i==x[-a]:
...                 count=count+0
...             else:
...                 count=count+1
...             a=a+1
...         if count==0:
...             return True
...         else:
...             return False
...             
