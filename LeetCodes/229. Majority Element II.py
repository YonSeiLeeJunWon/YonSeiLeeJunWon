Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def majorityElement(self, nums: List[int]) -> List[int]:
...         dic={}
...         for i in nums:
...             if i not in dic:
...                 dic[i]=1
...             else:
...                 dic[i]+=1
...         
...         value=int(len(nums)/3)
... 
...         lst=[]
...         for i, j in dic.items():
...             if j>value:
...                 lst.append(i)
...         return lst
