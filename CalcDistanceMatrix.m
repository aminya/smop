function mA = CalcDistanceMatrix(matrixSize, mX, mY)

mY = randn(matrixSize, matrixSize);

mA = sum(mX .^ 2, 1).' - (2 .* mX.' * mY) + sum(mY .^ 2, 1);

end