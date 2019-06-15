# Generated with SMOP  0.41
from libsmop import *
# MatrixMultiplication.m

    
@function
def MatrixMultiplication(matrixSize=None,mX=None,mY=None,*args,**kwargs):
    varargin = MatrixMultiplication.varargin
    nargin = MatrixMultiplication.nargin

    sacalrA=rand(1)
# MatrixMultiplication.m:3
    sacalrB=rand(1)
# MatrixMultiplication.m:4
    mA=dot((sacalrA + mX),(sacalrB + mY))
# MatrixMultiplication.m:6
    return mA
    
if __name__ == '__main__':
    pass
    