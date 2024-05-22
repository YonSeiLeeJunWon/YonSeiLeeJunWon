class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        join1=""
        join2=""
        for i in word1:
            join1=join1+i
        for i in word2:
            join2=join2+i
        if join1==join2:
            return True
        else:
            return False
        
