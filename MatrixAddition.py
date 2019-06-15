# Generated with SMOP  0.41
from libsmop import *
# MatrixAddition.m

    
@function
def MatrixAddition(matrixSize=None,mX=None,mY=None,*args,**kwargs):
    varargin = MatrixAddition.varargin
    nargin = MatrixAddition.nargin

    scalarA=rand(1)
# MatrixAddition.m:3
    scalarB=rand(1)
# MatrixAddition.m:4
    mA=(multiply(scalarA,mX)) + (multiply(scalarB,mY))
# MatrixAddition.m:6
    return mA
    
if __name__ == '__main__':
    pass
    