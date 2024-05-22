class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        maxvalue=-100
        for i in range(0,len(nums)):
            if maxvalue<nums[i]:
                maxvalue=nums[i]
            else:
                count=count+(maxvalue-nums[i]+1)
                maxvalue+=1
        return count
    
