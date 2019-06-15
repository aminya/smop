# Generated with SMOP  0.41
from libsmop import *
# CholDec.m

    
@function
def CholDec(matrixSize=None,mX=None,mY=None,*args,**kwargs):
    varargin = CholDec.varargin
    nargin = CholDec.nargin

    mY=dot(mX.T,mX)
# CholDec.m:3
    mA=chol(mY)
# CholDec.m:5
    return mA
    
if __name__ == '__main__':
    pass
    