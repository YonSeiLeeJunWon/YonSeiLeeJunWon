Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def countPairs(self, nums: List[int], k: int) -> int:
...         count=0
...         for i in range(len(nums)-1):
...             for j in range(i+1,len(nums)):
...                 if nums[i]==nums[j] and (i*j)%k==0:
...                     count+=1
...         return count