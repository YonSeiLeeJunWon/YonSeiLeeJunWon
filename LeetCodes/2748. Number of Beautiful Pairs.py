import math
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count=0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if math.gcd(int(str(nums[i])[0]),int(str(nums[j])[-1]))==1:
                    count+=1
        return count
    
