class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        lst=[0]
        total=0
        for i in gain:
            total+=i
            lst.append(total)
        return max(lst)
    
