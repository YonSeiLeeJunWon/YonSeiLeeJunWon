class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        findlist=[]
        for i in range(0,len(words)):
            if x in words[i]:
                findlist.append(i)
        return findlist
    
