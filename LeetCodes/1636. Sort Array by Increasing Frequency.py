Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def frequencySort(self, nums: List[int]) -> List[int]:
...         nums.sort(reverse=True)
...         value=[]
...         frequency=[]
...         answer=[]
...         for i in nums:
...             if i not in value:
...                 value.append(i)
... 
...         for j in value:
...             count=0
...             for i in nums:
...                 if i==j:
...                     count+=1
...             frequency.append(count)
...         while True:
...             if min(frequency)==1000:
...                 break
...             else:
...                 for _ in range(min(frequency)):
...                     answer.append(value[frequency.index(min(frequency))])
...                 frequency[frequency.index(min(frequency))]=1000
...         
...         return answer
