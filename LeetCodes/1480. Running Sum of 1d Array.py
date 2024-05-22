Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        Sum=0
        for i in range(0,len(nums)):
            for j in range(0,i+1):
                Sum+=nums[j]
            result.append(Sum)
            Sum=0
        return result

