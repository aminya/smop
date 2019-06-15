function mA = LinearSystem(matrixSize, mX, mY)

% mA = randn(matrixSize, matrixSize);
mB = randn(matrixSize, matrixSize);
vB = randn(matrixSize, 1);

vA = mX \ vB;
mA = mX \ mB;

mA = mA + vA;

end
