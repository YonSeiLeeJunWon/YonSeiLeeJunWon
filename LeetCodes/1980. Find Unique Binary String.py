Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def findDifferentBinaryString(self, nums: List[str]) -> str:
...         s=""
...         j=0
...         for i in nums:
...             if i[j]=="1":
...                 s+="0"
...                 j+=1
...             else:
...                 s+="1"
...                 j+=1
...         return s
