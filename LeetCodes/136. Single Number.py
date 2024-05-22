Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lst=set(nums)
        result=[]
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    lst.discard(int(nums[i]))
        for i in lst:
            result.append(i)
        return result[0]
    
