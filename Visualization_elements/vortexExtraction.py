import numpy as np
import array
from vorticityAndStrain import vorticityAndStrainTensors
from tensorOperations import tensorOperationsFast
from numpy import linalg as LA
from numba import jit

#---------------------------------------------------------------------#

# -----------------------------SPHYNX/CEA---------------------------- #

# Author: Abhishek Harikrishnan
# Email: abhishek.paraswararharikrishnan@cea.fr
# Last updated: 28-05-2024

#---------------------------------------------------------------------#

class vortexExtract:
	
	'''
	Extraction of vortices with numerous techniques. A broad list was neatly
	summarized in table 1 of Gunther and Theisel 2018. 
	
	Günther, Tobias, and Holger Theisel. "The state of the art in vortex 
	extraction." In Computer Graphics Forum, vol. 37, no. 6, pp. 149-173. 2018.
	
	Region-based methods:
	
	vorticity magnitude ω =  | ∇ x v |
	helicity h =  ( ∇ x v ) . v
	normalized helicity h_n = (( ∇ x v ) / | ∇ x v |) . (v / |v|)
	
	'''
	
	def __init__(self, u, v, w, dx, dy, dz):
		
		# For vorticity magnitude, Q - criterion,
		# Delta - criterion, Swirling strength criterion
		
		xlen, ylen, zlen = np.shape(u)
		
		dudx = np.zeros((xlen,ylen,zlen), dtype = dx.dtype)
		dvdx = np.zeros((xlen,ylen,zlen), dtype = dx.dtype)
		dwdx = np.zeros((xlen,ylen,zlen), dtype = dx.dtype)
		dudy = np.zeros((xlen,ylen,zlen), dtype = dx.dtype)
		dvdy = np.zeros((xlen,ylen,zlen), dtype = dx.dtype)
		dwdy = np.zeros((xlen,ylen,zlen), dtype = dx.dtype)
		dudz = np.zeros((xlen,ylen,zlen), dtype = dx.dtype)
		dvdz = np.zeros((xlen,ylen,zlen), dtype = dx.dtype)
		dwdz = np.zeros((xlen,ylen,zlen), dtype = dx.dtype)

		du =  np.gradient(u, dx, dy, dz)
		dv =  np.gradient(v, dx, dy, dz)
		dw =  np.gradient(w, dx, dy, dz)

		self.dudx = du[0]
		self.dudy = du[1]
		self.dudz = du[2]
		self.dvdx = dv[0]
		self.dvdy = dv[1]
		self.dvdz = dv[2]
		self.dwdx = dw[0]
		self.dwdy = dw[1]
		self.dwdz = dw[2]

		del du, dv, dw
		
		# For lambda2Criterion
		
		self.u = u
		self.v = v
		self.w = w
		self.dx = dx
		self.dy = dy
		self.dz = dz
		
	def vorticityComponents(self):
		
		w1 = np.subtract(self.dwdy, self.dvdz)
		w2 = np.subtract(self.dudz, self.dwdx)
		w3 = np.subtract(self.dvdx, self.dudy)
		
		return w1, w2, w3
	
	def vorticityMagnitude(self):
		
		w1 = np.subtract(self.dwdy, self.dvdz)
		w2 = np.subtract(self.dudz, self.dwdx)
		w3 = np.subtract(self.dvdx, self.dudy)

		wMag = np.sqrt(w1**2 + w2**2 + w3**2)
		
		return wMag
	
	def velocityMagnitude(self):
		
		return np.sqrt(self.u**2 + self.v**2 + self.w**2)
		
	def qCriterion(self):
	
		p1 = np.multiply(self.dudx, self.dvdy)
		p2 = np.multiply(self.dudx, self.dwdz)
		p3 = np.multiply(self.dvdy, self.dwdz)
		p4 = np.multiply(self.dwdy, self.dvdz)
		p5 = np.multiply(self.dudy, self.dvdx)
		p6 = np.multiply(self.dudz, self.dwdx)

		q = p1 + p2 + p3 - p4 - p5 - p6
		
		del p1, p2, p3, p4, p5, p6
		
		return q
		
	def deltaCriterion(self):
		
		q = self.qCriterion()

		# Delta criterion

		p1 = np.multiply(self.dudx, self.dvdy)
		p1_1 = np.multiply(p1, self.dwdz)
		del p1

		p2 = np.multiply(self.dudx, self.dwdy)
		p2_1 = np.multiply(p2, self.dvdz)
		del p2

		p3 = np.multiply(self.dudy, self.dvdx)
		p3_1 = np.multiply(p3, self.dwdz)
		del p3

		p4 = np.multiply(self.dvdz, self.dwdx)
		p4_1 = np.multiply(p4, self.dudy)
		del p4

		p5 = np.multiply(self.dudz, self.dvdx)
		p5_1 = np.multiply(p5, self.dwdy)
		del p5

		p6 = np.multiply(self.dudz, self.dwdx)
		p6_1 = np.multiply(p6, self.dvdy)
		del p6

		grad_deltaV = p1_1 - p2_1 - p3_1 + p4_1 + p5_1 - p6_1

		delta = (np.divide(q,3))**3 + (np.divide(grad_deltaV,2))**2
		
		del p1_1, p2_1, p3_1, p4_1, p5_1, p6_1, grad_deltaV
		
		return delta
	
	@staticmethod
	@jit(nopython=True)
	def lambda2EigComputation(lambda2, s2o2_11,\
	s2o2_12, s2o2_13, s2o2_21, s2o2_22, s2o2_23, s2o2_31,\
	s2o2_32, s2o2_33):
		
		for i in range(len(lambda2)):
			s2o2Tensor = np.array([[s2o2_11[i], s2o2_12[i], s2o2_13[i]],[s2o2_21[i], s2o2_22[i], s2o2_23[i]],[s2o2_31[i], s2o2_32[i], s2o2_33[i]]])
			eigVal, eigVec = LA.eig(s2o2Tensor)
			eigVal = sorted(eigVal)
			lambda2[i] = lambda2[i] + (eigVal[::-1][1])
		
		return lambda2
	
	def lambda2Criterion(self):
		
		# Calculate vorticity and strain tensors
		# NOTE: This method is slightly slower but q criterion values
		# do match
		
		velGradientObj = vorticityAndStrainTensors(self.u, self.v, \
		self.w, self.dx, self.dy, self.dz, self.dx.dtype)
		velocityGradientTensor = velGradientObj.velocityGradient()
		vorticityTensor = velGradientObj.vorticityTensor()
		strainTensor = velGradientObj.strainTensor()
		
		tensorObj = tensorOperationsFast(strainTensor)
		strainSquare = tensorObj.calculateTensorSquare()
		
		tensorObj = tensorOperationsFast(vorticityTensor)
		vortSquare = tensorObj.calculateTensorSquare()
		
		s2o2_11 = np.add(strainSquare[0], vortSquare[0]).ravel()
		s2o2_12 = np.add(strainSquare[1], vortSquare[1]).ravel()
		s2o2_13 = np.add(strainSquare[2], vortSquare[2]).ravel()
		s2o2_21 = np.add(strainSquare[3], vortSquare[3]).ravel()
		s2o2_22 = np.add(strainSquare[4], vortSquare[4]).ravel()
		s2o2_23 = np.add(strainSquare[5], vortSquare[5]).ravel()
		s2o2_31 = np.add(strainSquare[6], vortSquare[6]).ravel()
		s2o2_32 = np.add(strainSquare[7], vortSquare[7]).ravel()
		s2o2_33 = np.add(strainSquare[8], vortSquare[8]).ravel()
		
		# The next part is slow. Speeding up with Numba causes issues.
		
		lambda2 = np.zeros((np.shape(self.u)), dtype = self.dx.dtype)
		lambda2 = lambda2.ravel()
		
		lambda2 = self.lambda2EigComputation(lambda2, s2o2_11,\
					s2o2_12, s2o2_13, s2o2_21, s2o2_22, s2o2_23, s2o2_31,\
					s2o2_32, s2o2_33)
		
		return np.reshape(lambda2, np.shape(self.u))
	
	def helicity(self):
		
		w1, w2, w3 = self.vorticityComponents()
		
		return w1 * self.u + w2 * self.v + w3 * self.w
	
	def normalizedHelicity(self):
		
		w1, w2, w3 = self.vorticityComponents()
		wMag = self.vorticityMagnitude()
		velMag = self.velocityMagnitude()
		
		# Normalize first before computing dot product
		
		w1 = w1 / wMag
		w2 = w2 / wMag
		w3 = w3 / wMag
		
		u1 = self.u / velMag
		u2 = self.v / velMag
		u3 = self.w / velMag
		
		return w1 * u1 + w2 * u2 + w3 * u3
		
	def kinematicVorticityNumber(self):
		
		velGradientObj = vorticityAndStrainTensors(self.u, self.v, \
		self.w, self.dx, self.dy, self.dz, self.dx.dtype)
		velocityGradientTensor = velGradientObj.velocityGradient()
		vorticityTensor = velGradientObj.vorticityTensor()
		strainTensor = velGradientObj.strainTensor()
		
		tensorObj = tensorOperationsFast(vorticityTensor)
		vorticityTensorNorm = tensorObj.calculateEuclideanNorm()
		
		tensorObj = tensorOperationsFast(strainTensor)
		strainTensorNorm = tensorObj.calculateEuclideanNorm()
		
		return vorticityTensorNorm/strainTensorNorm
	
	def enstrophyDensity(self):
		
		w1, w2, w3 = self.vorticityComponents()
		
		return w1**2 + w2**2 + w3**2
	
	def enstrophyProductionRate(self):
		
		# P = vorticity * strain rate tensor * vorticity
		
		w1, w2, w3 = self.vorticityComponents()
		
		velGradientObj = vorticityAndStrainTensors(self.u, self.v, \
		self.w, self.dx, self.dy, self.dz, self.dx.dtype)
		strainTensor = velGradientObj.strainTensor()
		
		sw1 = strainTensor[0] * w1 + strainTensor[1] * w1 + strainTensor[2] * w1
		sw2 = strainTensor[3] * w2 + strainTensor[4] * w2 + strainTensor[5] * w2
		sw3 = strainTensor[6] * w3 + strainTensor[7] * w3 + strainTensor[8] * w3
		
		return sw1 * w1 + sw2 * w2 + sw3 * w3
		
	def help(self):
		
		print(vortexExtract.__doc__)
