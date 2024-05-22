Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def kthDistinct(self, arr: List[str], k: int) -> str:
...         lst=[]
...         count=0
...         for i in range(len(arr)):
...             for j in range(len(arr)):
...                 if arr[j]==arr[i]:
...                     count+=1
...             if count==1:
...                 lst.append(arr[i])
...             count=0
...         if len(lst)<k:
...             return ""
...         else:
...             return lst[k-1]
