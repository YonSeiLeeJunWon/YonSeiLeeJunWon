Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def findNumbers(self, nums: List[int]) -> int:
...         count=0
...         result=0
...         for i in nums:
...             for digits in str(i):
...                 count+=1
...             if count%2==0:
...                 result+=1
...             count=0
...         return result
