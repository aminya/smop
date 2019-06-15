# Generated with SMOP  0.41
from libsmop import *
# LinearSystem.m

    
@function
def LinearSystem(matrixSize=None,mX=None,mY=None,*args,**kwargs):
    varargin = LinearSystem.varargin
    nargin = LinearSystem.nargin

    # mA = randn(matrixSize, matrixSize);
    mB=randn(matrixSize,matrixSize)
# LinearSystem.m:4
    vB=randn(matrixSize,1)
# LinearSystem.m:5
    vA=numpy.linalg.solve(mX,vB)
# LinearSystem.m:7
    mA=numpy.linalg.solve(mX,mB)
# LinearSystem.m:8
    mA=mA + vA
# LinearSystem.m:10
    return mA
    
if __name__ == '__main__':
    pass
    