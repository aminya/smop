# Generated with SMOP  0.41
from libsmop import *
# MatrixSqrt.m

    
@function
def MatrixSqrt(matrixSize=None,mX=None,mY=None,*args,**kwargs):
    varargin = MatrixSqrt.varargin
    nargin = MatrixSqrt.nargin

    mY=dot(mX.T,mX)
# MatrixSqrt.m:3
    mA=sqrtm(mY)
# MatrixSqrt.m:5
    return mA
    
if __name__ == '__main__':
    pass
    