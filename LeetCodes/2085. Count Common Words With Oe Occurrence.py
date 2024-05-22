Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def countWords(self, words1: List[str], words2: List[str]) -> int:
...         result=0
...         for i in words1:
...             count1=0
...             count2=0
...             for j in words1:
...                 if j==i:
...                     count1+=1
...             for k in words2:
...                 if k==i:
...                     count2+=1
...             if count1==1 and count2==1:
...                 result+=1
...         return result
