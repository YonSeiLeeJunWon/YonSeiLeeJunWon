Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def maximumWealth(self, accounts: List[List[int]]) -> int:
...         max=-1
...         total=0
...         for i in accounts:
...             for j in i:
...                 total+=j
...                 if max<total:
...                     max=total
...             total=0
...         return max
