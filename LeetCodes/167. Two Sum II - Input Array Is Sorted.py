Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def twoSum(self, numbers: List[int], target: int) -> List[int]:
...         for i in range(len(numbers)):
...             if target-numbers[i] in numbers and numbers.index(target-numbers[i])!=i:
...                 result=[i+1,numbers.index(target-numbers[i])+1]
...                 result.sort()
...                 return result
