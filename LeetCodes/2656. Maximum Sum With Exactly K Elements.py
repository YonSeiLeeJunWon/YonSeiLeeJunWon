class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return int(max(nums)*k+(k-1)*k/2)
    
