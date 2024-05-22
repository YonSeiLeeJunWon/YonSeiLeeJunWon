Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def uniqueOccurrences(self, arr: List[int]) -> bool:
...         dic={}
...         result=0
...         for i in range(len(arr)):
...             if arr[i] not in dic:
...                 count=0
...                 for j in arr:
...                     if arr[i]==j:
...                         count+=1
...                 dic[arr[i]]=count
...         for i in dic:
...             for j in dic:
...                 if dic[i]==dic[j]:
...                     result+=1
...             if result!=1:
...                 return False
...             result=0
...         return True
