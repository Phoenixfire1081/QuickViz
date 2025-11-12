import numpy as np
from numba import jit
from math import sqrt

#---------------------------------------------------------------------#

# Author: Abhishek Harikrishnan
# Email: abhishek.harikrishnan@fu-berlin.de
# Last updated: 08-12-2023

#---------------------------------------------------------------------#

class tensorOperationsFast:
	
	'''
	Some basic operations required for vortex extraction.
	Numba is used to speed up loop operations.
	
	Calculate Euclidean norm: ||M|| = sqrt(tr(M M^T))
	
	'''
	
	def __init__(self, _tensor):
		
		# Split the arrays
		
		self.xlen, self.ylen, self.zlen = np.shape(_tensor[0])
		
		self.t11 = _tensor[0].ravel()
		self.t12 = _tensor[1].ravel()
		self.t13 = _tensor[2].ravel()
		
		self.t21 = _tensor[3].ravel()
		self.t22 = _tensor[4].ravel()
		self.t23 = _tensor[5].ravel()
		
		self.t31 = _tensor[6].ravel()
		self.t32 = _tensor[7].ravel()
		self.t33 = _tensor[8].ravel()
	
	@staticmethod
	@jit(nopython = True, cache = True)
	def dotFast(mat1, mat2):
		s = 0
		mat = np.empty(shape=(mat1.shape[1], mat2.shape[0]), dtype=mat1.dtype)
		for r1 in range(mat1.shape[0]):
			for c2 in range(mat2.shape[1]):
				s = 0
				for j in range(mat2.shape[0]):
					s += mat1[r1,j] * mat2[j,c2]
				mat[r1,c2] = s
		return mat
	
	@staticmethod
	@jit(nopython = True, cache = True)
	def actualEuclideanNorm(xlen, ylen, zlen, _dtype, t11, t12, t13, \
	t21, t22, t23, t31, t32, t33, dotFast):
		
		# Calculate Euclidean norm
		
		EuclideanNorm = np.zeros((xlen * ylen * zlen), dtype = _dtype)
		mat = np.zeros((3, 3), dtype = _dtype)
		
		for i in range(len(t11)):
			
			mat[0][0] = t11[i]
			mat[0][1] = t12[i]
			mat[0][2] = t13[i]
			mat[1][0] = t21[i]
			mat[1][1] = t22[i]
			mat[1][2] = t23[i]
			mat[2][0] = t31[i]
			mat[2][1] = t32[i]
			mat[2][2] = t33[i]
			
			EuclideanNorm[i] += sqrt(np.trace(dotFast(mat, mat.transpose())))
			
		return EuclideanNorm
		
	def calculateEuclideanNorm(self):
		
		EuclideanNorm = self.actualEuclideanNorm(self.xlen, self.ylen, self.zlen,\
		self.t11[0].dtype, self.t11, self.t12, self.t13, self.t21, self.t22,\
		self.t23, self.t31, self.t32, self.t33, self.dotFast)
	
		return np.reshape(EuclideanNorm, [self.xlen, self.ylen, self.zlen])
		
	@staticmethod
	@jit(nopython = True, cache = True)
	def actualTensorSquare(xlen, ylen, zlen, _dtype, t11, t12, t13, \
	t21, t22, t23, t31, t32, t33, dotFast):
		
		# Calculate Tensor Square
		
		t11_2 = np.zeros((xlen * ylen * zlen), dtype = _dtype)
		t12_2 = np.zeros((xlen * ylen * zlen), dtype = _dtype)
		t13_2 = np.zeros((xlen * ylen * zlen), dtype = _dtype)
		t21_2 = np.zeros((xlen * ylen * zlen), dtype = _dtype)
		t22_2 = np.zeros((xlen * ylen * zlen), dtype = _dtype)
		t23_2 = np.zeros((xlen * ylen * zlen), dtype = _dtype)
		t31_2 = np.zeros((xlen * ylen * zlen), dtype = _dtype)
		t32_2 = np.zeros((xlen * ylen * zlen), dtype = _dtype)
		t33_2 = np.zeros((xlen * ylen * zlen), dtype = _dtype)
		
		mat = np.zeros((3, 3), dtype = _dtype)
		
		for i in range(len(t11)):
			
			mat[0][0] = t11[i]
			mat[0][1] = t12[i]
			mat[0][2] = t13[i]
			mat[1][0] = t21[i]
			mat[1][1] = t22[i]
			mat[1][2] = t23[i]
			mat[2][0] = t31[i]
			mat[2][1] = t32[i]
			mat[2][2] = t33[i]
			
			oTensor_square = dotFast(mat, mat)
			
			t11_2[i] += oTensor_square[0][0]
			t12_2[i] += oTensor_square[0][1]
			t13_2[i] += oTensor_square[0][2]
			t21_2[i] += oTensor_square[1][0]
			t22_2[i] += oTensor_square[1][1]
			t23_2[i] += oTensor_square[1][2]
			t31_2[i] += oTensor_square[2][0]
			t32_2[i] += oTensor_square[2][1]
			t33_2[i] += oTensor_square[2][2]
			
		return [t11_2, t12_2, t13_2, t21_2, t22_2, t23_2, t31_2, t32_2, t33_2]
	
	def calculateTensorSquare(self):
	
		return self.actualTensorSquare(self.xlen, self.ylen, self.zlen,\
		self.t11[0].dtype, self.t11, self.t12, self.t13, self.t21, self.t22,\
		self.t23, self.t31, self.t32, self.t33, self.dotFast)
