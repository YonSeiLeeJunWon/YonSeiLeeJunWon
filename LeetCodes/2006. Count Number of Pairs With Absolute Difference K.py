class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    count+=1
                j+=1
            i+=1
        return count
    
