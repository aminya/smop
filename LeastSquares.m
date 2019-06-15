function mA = LeastSquares(matrixSize, mX, mY)

% mA = randn(matrixSize, matrixSize);
mB = randn(matrixSize, matrixSize);
vB = randn(matrixSize, 1);

vA = (mX.' * mX) \ (mX.' * vB);
mA = (mX.' * mX) \ (mX.' * mB);

mA = mA + vA;

end
