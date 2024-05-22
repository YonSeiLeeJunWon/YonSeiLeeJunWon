Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        cx1=max(ax1,bx1)
        cx2=min(ax2,bx2)
        cy1=max(ay1,by1)
        cy2=min(ay2,by2)
        Area_a=(ax2-ax1)*(ay2-ay1)
        Area_b=(bx2-bx1)*(by2-by1)
        if cx1>cx2 or cy1>cy2:
            Area_union=0
        else:
            Area_union=(cx2-cx1)*(cy2-cy1)
        return Area_a+Area_b-Area_union
