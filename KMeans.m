function mA = KMeans(matrixSize, mX, mY)

% Assuming Samples are slong Columns (Rows are features)
% mX              = randn(matrixSize, matrixSize);
numClusters     = max( round(matrixSize / 100), 1 ); % max between 1 and round(...)
vClusterId      = zeros(matrixSize, 1);
numIterations   = 10;


mA  = mX(:, randperm(matrixSize, numClusters)); %<! Cluster Centroids

for ii = 1:numIterations
    [~, vClusterId(:)] = min( sum(mA .^ 2, 1).' - (2 .* mA.' * mX), [] , 1);
    for jj = 1:numClusters
        mA(:, jj) = mean(mX(:, vClusterId == jj), 2);
    end

end

mA = mA(:, 1) + mA(:, end).';

end