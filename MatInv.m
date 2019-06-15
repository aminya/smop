function mA = MatInv(matrixSize, mX, mY)

mY = mX.' * mX;

mA = inv(mY);
mB = pinv(mX);

mA = mA + mB;

end