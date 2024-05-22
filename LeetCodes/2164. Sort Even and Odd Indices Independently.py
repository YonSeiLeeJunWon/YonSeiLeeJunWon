Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def sortEvenOdd(self, nums: List[int]) -> List[int]:
...         Even_nums=[]
...         Odd_nums=[]
...         result=[]
...         for i in range(len(nums)):
...             if i%2==0:
...                 Even_nums.append(nums[i])
...             else:
...                 Odd_nums.append(nums[i])
...         Even_nums.sort()
...         Odd_nums.sort(reverse=True)
...         order_even=0
...         order_odd=0
...         for i in range(len(nums)):
...             if i%2==0:
...                 result.append(Even_nums[order_even])
...                 order_even+=1
...             else:
...                 result.append(Odd_nums[order_odd])
...                 order_odd+=1
...         return result
