class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        Lst=[]
        minvalue=min(len(word1),len(word2))
        for i in range(minvalue):
            Lst.append(word1[i])
            Lst.append(word2[i])
        if len(word1)>len(word2):
            for i in range(minvalue,len(word1)):
                Lst.append(word1[i])
        elif len(word1)<len(word2):
            for i in range(minvalue,len(word2)):
                Lst.append(word2[i])
        return "".join(Lst)
    
