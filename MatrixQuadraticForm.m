function mA = MatrixQuadraticForm( matrixSize, mX, mY )

vX = randn(matrixSize, 1);
vB = randn(matrixSize, 1);
sacalrC = rand(1);

mA = ((mX * vX).' * (mX * vX)) + (vB.' * vX) + sacalrC;

end