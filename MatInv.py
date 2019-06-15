# Generated with SMOP  0.41
from libsmop import *
# MatInv.m

    
@function
def MatInv(matrixSize=None,mX=None,mY=None,*args,**kwargs):
    varargin = MatInv.varargin
    nargin = MatInv.nargin

    mY=dot(mX.T,mX)
# MatInv.m:3
    mA=inv(mY)
# MatInv.m:5
    mB=pinv(mX)
# MatInv.m:6
    mA=mA + mB
# MatInv.m:8
    return mA
    
if __name__ == '__main__':
    pass
    