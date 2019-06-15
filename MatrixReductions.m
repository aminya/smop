function mA = MatrixReductions( matrixSize, mX, mY )

mA = sum(mX, 1) + min(mY, [], 2);

end
