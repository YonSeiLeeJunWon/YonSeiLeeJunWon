Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
    class Solution:
        def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
            count=0
            List=[]
            for i in range(0,len(nums)):
                for j in range(0,len(nums)):
                    if nums[i]>nums[j]:
                        count+=1
                    j+=1
                List.append(count)
                count=0
                i+=1
            return List

