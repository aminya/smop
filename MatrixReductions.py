# Generated with SMOP  0.41
from libsmop import *
# MatrixReductions.m

    
@function
def MatrixReductions(matrixSize=None,mX=None,mY=None,*args,**kwargs):
    varargin = MatrixReductions.varargin
    nargin = MatrixReductions.nargin

    mA=sum(mX,1) + min(mY,[],2)
# MatrixReductions.m:3
    return mA
    
if __name__ == '__main__':
    pass
    