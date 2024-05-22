class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            left_total=0
            right_total=0
            if i==0:
                left_total=0
                for j in range(1,len(nums)):
                    right_total+=nums[j]
            elif i==len(nums)-1:
                right_total=0
                for j in range(0,len(nums)-1):
                    left_total+=nums[j]
            else:
                for j in range(0,i):
                    left_total+=nums[j]
                for k in range(i+1,len(nums)):
                    right_total+=nums[k]
            if left_total==right_total:
                return i
        return -1
    
