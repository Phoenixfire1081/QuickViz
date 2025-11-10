from numba import jit, prange
import numpy as np

@jit(nopython = True, cache = True, fastmath = True)
def inverseDFT(xlen, ylen, zlen, kx, ky, kz, xx, yy, zz, ux, uy, uz):
		
	velx = np.zeros((xlen, ylen, zlen), dtype = np.float32)
	vely = np.zeros((xlen, ylen, zlen), dtype = np.float32)
	velz = np.zeros((xlen, ylen, zlen), dtype = np.float32)
	
	for xslice in range(xlen):

		for yslice in prange(ylen):
		
			matmulx = np.outer(kx, xx[xslice, yslice, :])
			matmuly = np.outer(ky, yy[xslice, yslice, :])
			matmulz = np.outer(kz, zz[xslice, yslice, :])
			
			mx = np.exp(1j * (matmulx + matmuly + matmulz))

			velx[xslice, yslice, :] += np.real(np.dot(mx.T, ux))
			vely[xslice, yslice, :] += np.real(np.dot(mx.T, uy))
			velz[xslice, yslice, :] += np.real(np.dot(mx.T, uz))
	
	return velx, vely, velz
