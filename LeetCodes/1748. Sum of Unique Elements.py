class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        total=0
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            if count==1:
                total+=nums[i]
            count=0
        return total

                
