Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def sortArrayByParity(self, nums: List[int]) -> List[int]:
...         lst_even=[]
...         lst_odd=[]
...         for i in nums:
...             if i%2==0:
...                 lst_even.append(i)
...             else:
...                 lst_odd.append(i)
...         lst_even.sort()
...         lst_odd.sort()
...         return lst_even+lst_odd
