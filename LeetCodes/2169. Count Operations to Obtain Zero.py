Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def countOperations(self, num1: int, num2: int) -> int:
...         count=0
...         while num1!=0 and num2!=0:
...             if num1>=num2:
...                 num1=num1-num2
...                 count+=1
...             else:
...                 num2=num2-num1
...                 count+=1
...         return count
