# Generated with SMOP  0.41
from libsmop import *
# LeastSquares.m

    
@function
def LeastSquares(matrixSize=None,mX=None,mY=None,*args,**kwargs):
    varargin = LeastSquares.varargin
    nargin = LeastSquares.nargin

    # mA = randn(matrixSize, matrixSize);
    mB=randn(matrixSize,matrixSize)
# LeastSquares.m:4
    vB=randn(matrixSize,1)
# LeastSquares.m:5
    vA=numpy.linalg.solve((dot(mX.T,mX)),(dot(mX.T,vB)))
# LeastSquares.m:7
    mA=numpy.linalg.solve((dot(mX.T,mX)),(dot(mX.T,mB)))
# LeastSquares.m:8
    mA=mA + vA
# LeastSquares.m:10
    return mA
    
if __name__ == '__main__':
    pass
    