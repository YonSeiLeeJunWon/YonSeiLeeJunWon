class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_word=-1
        word=1
        for i in sentences:
            for j in i:
                if j==" ":
                    word+=1
            if max_word<word:
                max_word=word
            word=1
        return max_word
    
