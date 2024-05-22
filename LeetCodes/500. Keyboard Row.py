Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        Lst=[]
        first_row="qwertyuiop"
        second_row="asdfghjkl"
        third_row="zxcvbnm"
        count1=0
        count2=0
        count3=0

        for i in words:
            for j in i:
                if j.lower() in first_row:
                    count1+=1
                elif j.lower() in second_row:
                    count2+=1
                else:
                    count3+=1
            if (count1==0 and count2==0) or (count2==0 and count3==0) or (count1==0 and count3==0):
                Lst.append(i)
            count1=0
            count2=0
            count3=0
        return Lst
    
