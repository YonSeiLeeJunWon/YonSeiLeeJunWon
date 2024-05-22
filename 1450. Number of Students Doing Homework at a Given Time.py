Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
...         count=0
...         for i in range(len(startTime)):
...             if startTime[i]<=queryTime<=endTime[i]:
...                 count+=1
...         return count
