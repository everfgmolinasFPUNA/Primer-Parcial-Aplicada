import pylab as pl
import numpy as np


X = np.linspace(-4, 0, 256, endpoint=True)
Y = np.linspace(0, 3, 256, endpoint=True)
W = np.linspace(3, 5, 256, endpoint=True)
Z = np.linspace(5, 9, 256, endpoint=True)

A, B, C, D = 0*X, Y/3, (5-W)/2, 0*Z

pl.plot(X, A)
pl.plot(Y, B)
pl.plot(W, C)
pl.plot(Z, D)

pl.show()