class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        minvalue=101
        maxvalue=-1
        if len(nums)==1:
            return -1
        for i in nums:
            if i<minvalue:
                minvalue=i
            if i>maxvalue:
                maxvalue=i
        nums.remove(minvalue)
        nums.remove(maxvalue)
        if len(nums)==0:
            return -1
        else:
            return nums[0]
        
