class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        Sum=0
        for i in operations:
            if i=="--X" or i=="X--":
                Sum=Sum-1
            else:
                Sum=Sum+1
        return Sum
    
