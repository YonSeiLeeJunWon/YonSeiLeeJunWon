Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
...         n=len(nums)
...         prefix_sum=[0]*(n+1)
...         for i in range(1,n+1):
...             prefix_sum[i]=prefix_sum[i-1] + nums[i-1]
...         
...         result = []
...         for i in range(n):
...             left_sum = prefix_sum[i]
...             right_sum = prefix_sum[n]-prefix_sum[i+1]
...             result.append((nums[i]*i-left_sum) + (right_sum-nums[i]*(n-i-1)))
...         
...         return result
