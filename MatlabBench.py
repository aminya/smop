# Generated with SMOP  0.41
from libsmop import *
# MatlabBench.m

    
@function
def MatlabBench(operationMode=None,*args,**kwargs):
    varargin = MatlabBench.varargin
    nargin = MatlabBench.nargin

    allFunctions=cellarray([MatrixGeneration,MatrixAddition,MatrixMultiplication,MatrixQuadraticForm,MatrixReductions,ElementWiseOperations,MatrixExp,MatrixSqrt,Svd,Eig,CholDec,MatInv,LinearSystem,LeastSquares,CalcDistanceMatrix,KMeans])
# MatlabBench.m:3
    allFunctionsString=cellarray(['Matrix Generation','Matrix Addition','Matrix Multiplication','Matrix Quadratic Form','Matrix Reductions','Element Wise Operations','Matrix Exponential','Matrix Square Root','SVD','Eigen Decomposition','Cholesky Decomposition','Matrix Inversion','Linear System Solution','Linear Least Squares','Squared Distance Matrix','K-Means Run Time'])
# MatlabBench.m:8
    numFun=length(allFunctions)
# MatlabBench.m:14
    if (operationMode == 1):
        vMatrixSize=csvread(fullfile('Inputs','vMatrixSizePartial.csv'))
# MatlabBench.m:17
        numIterations=csvread(fullfile('Inputs','numIterationsPartial.csv'))
# MatlabBench.m:18
    else:
        if (operationMode == 2):
            vMatrixSize=csvread(fullfile('Inputs','vMatrixSizeFull.csv'))
# MatlabBench.m:20
            numIterations=csvread(fullfile('Inputs','numIterationsFull.csv'))
# MatlabBench.m:21
        else:
            if (operationMode == 0):
                vMatrixSize=2
# MatlabBench.m:23
                numIterations=1
# MatlabBench.m:24
    
    vTestIdx=arange(1,numFun)
# MatlabBench.m:27
    
    cRunTimeFunctions=allFunctions(vTestIdx)
# MatlabBench.m:28
    cFunctionString=allFunctionsString(vTestIdx)
# MatlabBench.m:29
    mRunTime=zeros(length(vMatrixSize),length(cRunTimeFunctions),numIterations)
# MatlabBench.m:31
    cRunTime=cell(length(allFunctions) + 1,length(vMatrixSize) + 1)
# MatlabBench.m:32
    
    cRunTime[1,1]='FunctionName\\MatrixSize'
# MatlabBench.m:33
    for ii in arange(1,length(vMatrixSize)).reshape(-1):
        matrixSize=vMatrixSize(ii)
# MatlabBench.m:37
        mX=randn(matrixSize,matrixSize)
# MatlabBench.m:38
        mY=randn(matrixSize,matrixSize)
# MatlabBench.m:39
        disp(concat(['Matrix Size - ',num2str(matrixSize)]))
        for jj in arange(1,length(cRunTimeFunctions)).reshape(-1):
            disp(concat(['Processing ',num2str(cFunctionString[jj]),' Matrix Size ',num2str(matrixSize)]))
            for kk in arange(1,numIterations).reshape(-1):
                fun=lambda : cRunTimeFunctions[jj](matrixSize,mX,mY)
# MatlabBench.m:47
                mRunTime[ii,jj,kk]=dot(timeit(fun),1000000.0)
# MatlabBench.m:48
            cRunTime[jj + 1,1]=num2str(cFunctionString[jj])
# MatlabBench.m:52
            cRunTime[1,ii + 1]=matrixSize
# MatlabBench.m:53
            cRunTime[jj + 1,ii + 1]=mean(mRunTime(ii,jj,arange()))
# MatlabBench.m:54
    
    tRunTime=cell2table(cRunTime)
# MatlabBench.m:58
    return mRunTime,tRunTime
    
if __name__ == '__main__':
    pass
    