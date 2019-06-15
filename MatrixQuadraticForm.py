# Generated with SMOP  0.41
from libsmop import *
# MatrixQuadraticForm.m

    
@function
def MatrixQuadraticForm(matrixSize=None,mX=None,mY=None,*args,**kwargs):
    varargin = MatrixQuadraticForm.varargin
    nargin = MatrixQuadraticForm.nargin

    vX=randn(matrixSize,1)
# MatrixQuadraticForm.m:3
    vB=randn(matrixSize,1)
# MatrixQuadraticForm.m:4
    sacalrC=rand(1)
# MatrixQuadraticForm.m:5
    mA=(dot((dot(mX,vX)).T,(dot(mX,vX)))) + (dot(vB.T,vX)) + sacalrC
# MatrixQuadraticForm.m:7
    return mA
    
if __name__ == '__main__':
    pass
    