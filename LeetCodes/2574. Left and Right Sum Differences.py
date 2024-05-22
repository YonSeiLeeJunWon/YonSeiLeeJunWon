class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=0
        left=[]
        rightsum=0
        right=[]
        total=[]
        for i in range(0,len(nums)):
            left.append(leftsum)
            leftsum+=nums[i]
        for j in range(0,len(nums)):
            right.append(rightsum)
            rightsum+=nums[len(nums)-1-j]
        for k in range(0,len(left)):
            total.append(abs(left[k]-right[len(left)-k-1]))
        return total
    
