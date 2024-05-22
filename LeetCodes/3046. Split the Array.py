Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def isPossibleToSplit(self, nums: List[int]) -> bool:
...         dic={}
...         for i in nums:
...             if i not in dic:
...                 dic[i]=1
...             else:
...                 dic[i]+=1
...         
...         for j in dic.values():
...             if j>=3:
...                 return False
...         return True
