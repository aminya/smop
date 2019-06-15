# Generated with SMOP  0.41
from libsmop import *
# ElementWiseOperations.m

    
@function
def ElementWiseOperations(matrixSize=None,mX=None,mY=None,*args,**kwargs):
    varargin = ElementWiseOperations.varargin
    nargin = ElementWiseOperations.nargin

    # Make sure roots are positive
    mA=rand(matrixSize,matrixSize)
# ElementWiseOperations.m:4
    mB=3 + rand(matrixSize,matrixSize)
# ElementWiseOperations.m:5
    mC=rand(matrixSize,matrixSize)
# ElementWiseOperations.m:6
    mD=abs(mA) + sin(mB)
# ElementWiseOperations.m:8
    mE=exp(- (mA ** 2))
# ElementWiseOperations.m:9
    mF=(- mB + sqrt((mB ** 2) - (multiply(multiply(4,mA),mC)))) / (multiply(2,mA))
# ElementWiseOperations.m:10
    mA=mD + mE + mF
# ElementWiseOperations.m:12
    return mA
    
if __name__ == '__main__':
    pass
    