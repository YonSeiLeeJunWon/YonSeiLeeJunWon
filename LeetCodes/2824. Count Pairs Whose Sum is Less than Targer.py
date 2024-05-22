Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def countPairs(self, nums: List[int], target: int) -> int:
...         count=0
...         for i in range(0,len(nums)):
...             for j in range(i+1,len(nums)):
...                 total=0
...                 total=nums[i]+nums[j]
...                 if total<target:
...                      count+=1
...         return count
