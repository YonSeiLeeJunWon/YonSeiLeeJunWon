Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
...         for i in range(len(event1)):
...             strings=event1[i].split(":")
...             time=60*int(strings[0])+int(strings[1])
...             event1[i]=time
...         
...         for j in range(len(event2)):
...             strings=event2[j].split(":")
...             time=60*int(strings[0])+int(strings[1])
...             event2[j]=time
... 
...         if (event1[0]<=event2[0] and event1[1]>=event2[0]) or (event1[0]<=event2[1] and event1[1]>=event2[1]) or (event1[0]<=event2[0] and event1[1]>=event2[1]) or (event1[0]>=event2[0] and event1[1]<=event2[1]):
...             return True
...         else:
...             return False
