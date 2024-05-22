Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def moveZeroes(self, nums: List[int]) -> None:
...         """
...         Do not return anything, modify nums in-place instead.
...         """
...         count0=0
...         while 0 in nums:
...             nums.remove(0)
...             count0+=1
...         
...         for i in range(count0):
...             nums.append(0)
