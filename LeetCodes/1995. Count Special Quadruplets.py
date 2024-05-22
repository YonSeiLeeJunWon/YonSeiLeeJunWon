Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def countQuadruplets(self, nums: List[int]) -> int:
...         count=0
...         for i in range(len(nums)-3):
...             for j in range(i+1,len(nums)-2):
...                 for k in range(j+1,len(nums)-1):
...                     for l in range(k+1,len(nums)):
...                         if nums[i]+nums[j]+nums[k]==nums[l]:
...                             count+=1
...         return count
