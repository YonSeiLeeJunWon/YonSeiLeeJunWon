Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def findPeaks(self, mountain: List[int]) -> List[int]:
...         result=[]
...         for i in range(1,len(mountain)-1):
...             if mountain[i-1]<mountain[i] and mountain[i]>mountain[i+1]:
...                 result.append(i)
...         return result
