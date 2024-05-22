Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
...         lst=[]
...         for i in words:
...             for j in i:
...                 if j not in allowed:
...                     lst.append(j)
...                     break
...                 
...         return len(words)-len(lst)
