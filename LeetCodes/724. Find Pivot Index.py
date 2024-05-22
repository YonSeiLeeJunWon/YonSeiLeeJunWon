Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def pivotIndex(self, nums: List[int]) -> int:
...         for i in range(0,len(nums)):
...             if i==0:
...                 if sum(nums[i+1:len(nums)])==0:
...                     return 0
...             elif i==len(nums):
...                 if sum(nums[0:i])==0:
...                     return 0
...             elif sum(nums[0:i])==sum(nums[i+1:len(nums)]):
...                 return i
...         return -1
...             
