# Generated with SMOP  0.41
from libsmop import *
# MatrixExp.m

    
@function
def MatrixExp(matrixSize=None,mX=None,mY=None,*args,**kwargs):
    varargin = MatrixExp.varargin
    nargin = MatrixExp.nargin

    mA=expm(mX)
# MatrixExp.m:3
    return mA
    
if __name__ == '__main__':
    pass
    