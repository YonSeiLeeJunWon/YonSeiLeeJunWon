Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def findFinalValue(self, nums: List[int], original: int) -> int:
...         answer=0
...         i=1
...         while True:
...             if original not in nums:
...                 if answer==0:
...                     return original
...                 else:
...                     return answer
...             else:
...                 answer=original*2
...             original=original*2
