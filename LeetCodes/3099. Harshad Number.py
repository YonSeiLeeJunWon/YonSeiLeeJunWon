class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        Sum=0
        for i in str(x):
            Sum=Sum+int(i)
        if x%Sum==0:
            return Sum
        else:
            return -1
        
