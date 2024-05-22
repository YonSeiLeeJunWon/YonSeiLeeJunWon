class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum=0
        digitSum=0
        for i in range(0,len(nums)):
            elementSum+=nums[i]
        for i in nums:
            for j in str(i):
                digitSum+=int(j)
        return abs(elementSum-digitSum)
    
