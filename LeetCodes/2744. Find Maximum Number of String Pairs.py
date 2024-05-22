Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def maximumNumberOfStringPairs(self, words: List[str]) -> int:
...         count=0
...         for i in range(len(words)-1):
...             set_1=set(words[i])
...             for j in range(i+1,len(words)):
...                 set_2=set(words[j])
...                 if set_1==set_2:
...                     count+=1
...         return count
