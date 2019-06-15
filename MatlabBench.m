function [ mRunTime,tRunTime ] = MatlabBench( operationMode )

allFunctions = {@MatrixGeneration, @MatrixAddition,@MatrixMultiplication,...
    @MatrixQuadraticForm, @MatrixReductions, @ElementWiseOperations, @MatrixExp,...
    @MatrixSqrt, @Svd, @Eig,@CholDec, @MatInv, @LinearSystem, @LeastSquares,...
    @CalcDistanceMatrix, @KMeans};

allFunctionsString = {'Matrix Generation', 'Matrix Addition', 'Matrix Multiplication',...
    'Matrix Quadratic Form', 'Matrix Reductions', 'Element Wise Operations',...
    'Matrix Exponential', 'Matrix Square Root', 'SVD', 'Eigen Decomposition',...
    'Cholesky Decomposition', 'Matrix Inversion','Linear System Solution',...
    'Linear Least Squares', 'Squared Distance Matrix', 'K-Means Run Time'};

numFun = length(allFunctions);

if(operationMode == 1)     % Partial Benchmark
    vMatrixSize = csvread(fullfile('Inputs', 'vMatrixSizePartial.csv'));
    numIterations = csvread(fullfile('Inputs', 'numIterationsPartial.csv'));
elseif(operationMode == 2) % Full Benchmark
    vMatrixSize = csvread(fullfile('Inputs', 'vMatrixSizeFull.csv'));
    numIterations = csvread(fullfile('Inputs','numIterationsFull.csv'));
elseif(operationMode == 0) % Test Benchmark
    vMatrixSize = 2;
    numIterations =  1;
end

vTestIdx=1:numFun; % change this to do different tests
cRunTimeFunctions = allFunctions(vTestIdx);
cFunctionString = allFunctionsString(vTestIdx);

mRunTime = zeros(length(vMatrixSize), length(cRunTimeFunctions), numIterations);
cRunTime= cell(length(allFunctions)+1,length(vMatrixSize)+1); % a table containing all the information
cRunTime{1,1}="FunctionName\\MatrixSize";


for ii = 1:length(vMatrixSize)
    matrixSize = vMatrixSize(ii);
    mX = randn(matrixSize, matrixSize);
    mY = randn(matrixSize, matrixSize);
    disp(['Matrix Size - ', num2str(matrixSize)]);

    for jj = 1:length(cRunTimeFunctions)
        disp(['Processing ', num2str(cFunctionString{jj}), ' Matrix Size ', num2str(matrixSize)]);

        for kk = 1:numIterations

            fun=@() cRunTimeFunctions{jj}(matrixSize, mX, mY);
            mRunTime(ii, jj, kk) = timeit(fun)*1e6; % computes median of bench times
            

        end
        cRunTime{jj+1,1}=num2str(cFunctionString{jj});
		cRunTime{1,ii+1}=matrixSize;
		cRunTime{jj+1,ii+1}=mean(mRunTime(ii, jj,:));
    end
end

tRunTime=cell2table(cRunTime);
end
