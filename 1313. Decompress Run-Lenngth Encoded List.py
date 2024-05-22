Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def decompressRLElist(self, nums: List[int]) -> List[int]:
...         lst=[]
...         for i in range(0,len(nums),2):
...             for j in range(nums[i]):
...                 lst.append(nums[i+1])
...         return lst
