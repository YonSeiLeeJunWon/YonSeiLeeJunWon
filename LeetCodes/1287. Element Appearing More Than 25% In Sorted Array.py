Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def findSpecialInteger(self, arr: List[int]) -> int:
...         count=1
...         if len(arr)==1:
...             return arr[0]
...             
...         for i in range(1,len(arr)):
...             if arr[i-1]==arr[i]:
...                 count+=1
...             else:
...                 count=1
...             
...             if count>0.25*len(arr):
...                 return arr[i]
