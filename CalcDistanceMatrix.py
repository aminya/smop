# Generated with SMOP  0.41
from libsmop import *
# CalcDistanceMatrix.m

    
@function
def CalcDistanceMatrix(matrixSize=None,mX=None,mY=None,*args,**kwargs):
    varargin = CalcDistanceMatrix.varargin
    nargin = CalcDistanceMatrix.nargin

    mY=randn(matrixSize,matrixSize)
# CalcDistanceMatrix.m:3
    mA=sum(mX ** 2,1).T - (dot(multiply(2,mX.T),mY)) + sum(mY ** 2,1)
# CalcDistanceMatrix.m:5
    return mA
    
if __name__ == '__main__':
    pass
    