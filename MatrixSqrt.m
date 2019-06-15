function mA = MatrixSqrt(matrixSize, mX, mY)

mY = mX.' * mX;

mA = sqrtm(mY);

end