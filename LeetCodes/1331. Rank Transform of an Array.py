Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def arrayRankTransform(self, arr: List[int]) -> List[int]:
...         lst=arr.copy()
...         lst.sort()
...         dic={}
...         result=[]
...         j=1
...         for i in range(len(lst)):
...             if lst[i] not in dic:
...                 dic[lst[i]]=j
...                 j+=1
...         for j in range(len(arr)):
...             arr[j]=dic[arr[j]]
...         return arr
