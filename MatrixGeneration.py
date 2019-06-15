# Generated with SMOP  0.41
from libsmop import *
# MatrixGeneration.m

    
    
@function
def MatrixGeneration(matrixSize=None,mX=None,mY=None,*args,**kwargs):
    varargin = MatrixGeneration.varargin
    nargin = MatrixGeneration.nargin

    mA=randn(matrixSize,matrixSize)
# MatrixGeneration.m:4
    mB=rand(matrixSize,matrixSize)
# MatrixGeneration.m:5
    return mA
    
if __name__ == '__main__':
    pass
    