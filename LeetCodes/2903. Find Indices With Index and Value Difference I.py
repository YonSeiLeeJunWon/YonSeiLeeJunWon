Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
...         result=[]
...         for i in range(len(nums)):
...             for j in range(len(nums)):
...                 if abs(i-j)>=indexDifference and abs(nums[i]-nums[j])>=valueDifference:
...                     result.append(i)
...                     result.append(j)
...         if result==[]:
...             return [-1,-1]
...         else:
...             return result
