import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minvalue=1001
        maxvalue=-1
        for i in nums:
            if i<minvalue:
                minvalue=i
            if i>maxvalue:
                maxvalue=i
        return math.gcd(minvalue,maxvalue)
    
