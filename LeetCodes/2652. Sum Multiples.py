Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def sumOfMultiples(self, n: int) -> int:
...         sum=0
...         for i in range(1,n+1):
...             if i%3==0 or i%5==0 or i%7==0:
...                 sum=sum+i
...         return sum
