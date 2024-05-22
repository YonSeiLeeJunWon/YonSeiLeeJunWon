import numpy as np ## In Matrix, use numpy

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        A = np.array(matrix)
        A_column_max = np.max(A, axis=0)

        B= A.copy()
        m, n = A.shape
        for i in range(m):
            for j in range(n):
                if A[i,j] == -1:
                    B[i,j]=A_column_max[j]
        return B
    
