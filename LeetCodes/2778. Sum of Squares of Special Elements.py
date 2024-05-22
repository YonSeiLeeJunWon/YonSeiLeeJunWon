Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def sumOfSquares(self, nums: List[int]) -> int:
...         total=0
...         for i in range(1,len(nums)+1):
...             if len(nums)%i==0:
...                 total+=nums[i-1]*nums[i-1]
...         return total
