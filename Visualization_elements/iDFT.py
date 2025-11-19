from numba import jit, prange
import numpy as np
try:
	import cupy as cp
except:
	print('Attempting calculation with CPU and numba.')

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

# TODO - The functions need to be merged
@jit(nopython = True, cache = True, fastmath = True)
def inverseDFTsingleScalar(xlen, ylen, zlen, kx, ky, kz, xx, yy, zz, singleScalar):
	
	scalar = np.zeros((xlen, ylen, zlen), dtype = np.float32)
	
	for xslice in range(xlen):

		for yslice in prange(ylen):
		
			matmulx = np.outer(kx, xx[xslice, yslice, :])
			matmuly = np.outer(ky, yy[xslice, yslice, :])
			matmulz = np.outer(kz, zz[xslice, yslice, :])
			
			mx = np.exp(1j * (matmulx + matmuly + matmulz))

			scalar[xslice, yslice, :] += np.real(np.dot(mx.T, singleScalar))
	
	return scalar

def inverseDFTcupy(xlen, ylen, zlen, kx, ky, kz, xx, yy, zz, ux, uy, uz):
		
	velx = cp.zeros((xlen, ylen, zlen), dtype = cp.float32)
	vely = cp.zeros((xlen, ylen, zlen), dtype = cp.float32)
	velz = cp.zeros((xlen, ylen, zlen), dtype = cp.float32)
	
	# Convert everything as cupy arrays
	
	kx = cp.array(kx)
	ky = cp.array(ky)
	kz = cp.array(kz)
	
	xx = cp.array(xx)
	yy = cp.array(yy)
	zz = cp.array(zz)
	
	ux = cp.array(ux)
	uy = cp.array(uy)
	uz = cp.array(uz)
	
	for xslice in range(xlen):

		for yslice in range(ylen):
		
			matmulx = cp.outer(kx, xx[xslice, yslice, :])
			matmuly = cp.outer(ky, yy[xslice, yslice, :])
			matmulz = cp.outer(kz, zz[xslice, yslice, :])
			
			mx = cp.exp(1j * (matmulx + matmuly + matmulz))

			velx[xslice, yslice, :] += cp.real(cp.dot(mx.T, ux))
			vely[xslice, yslice, :] += cp.real(cp.dot(mx.T, uy))
			velz[xslice, yslice, :] += cp.real(cp.dot(mx.T, uz))
	
	return cp.asnumpy(velx), cp.asnumpy(vely), cp.asnumpy(velz)

def inverseDFTsingleScalarcupy(xlen, ylen, zlen, kx, ky, kz, xx, yy, zz, singleScalar):
		
	scalar = cp.zeros((xlen, ylen, zlen), dtype = cp.float32)
	
	# Convert everything as cupy arrays
	
	kx = cp.array(kx)
	ky = cp.array(ky)
	kz = cp.array(kz)
	
	xx = cp.array(xx)
	yy = cp.array(yy)
	zz = cp.array(zz)
	
	singleScalar = cp.array(singleScalar)
	
	for xslice in range(xlen):

		for yslice in range(ylen):
		
			matmulx = cp.outer(kx, xx[xslice, yslice, :])
			matmuly = cp.outer(ky, yy[xslice, yslice, :])
			matmulz = cp.outer(kz, zz[xslice, yslice, :])
			
			mx = cp.exp(1j * (matmulx + matmuly + matmulz))

			scalar[xslice, yslice, :] += cp.real(cp.dot(mx.T, singleScalar))
	
	return cp.asnumpy(scalar)
