function mA = CholDec(matrixSize, mX, mY)

mY = mX.' * mX;

mA = chol(mY);

end