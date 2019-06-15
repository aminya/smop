# Generated with SMOP  0.41
from libsmop import *
# Svd.m

    
@function
def Svd(matrixSize=None,mX=None,mY=None,*args,**kwargs):
    varargin = Svd.varargin
    nargin = Svd.nargin

    mU,mS,mV=svd(mX,nargout=3)
# Svd.m:3
    mA=0
# Svd.m:5
    return mA
    
if __name__ == '__main__':
    pass
    