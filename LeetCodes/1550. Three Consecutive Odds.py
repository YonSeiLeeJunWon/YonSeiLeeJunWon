Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def threeConsecutiveOdds(self, arr: List[int]) -> bool:
...         odd_count=0
...         for i in arr:
...             if i%2==0:
...                 odd_count=0
...             else:
...                 odd_count+=1
...             if odd_count==3:
...                 return True
...         return False
