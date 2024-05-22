class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        lst=[]
        minvalue=101
        for i in range(0,len(nums)):
            if i%10==nums[i]:
                lst.append(i)
        if len(lst)==len(nums):
            return 0
        elif len(lst)==0:
            return -1
        else:
            minvalue=101
            for i in lst:
                if i<minvalue:
                    minvalue=i
            return minvalue
        
