import numpy as np
import array
from tensorOperations import tensorOperationsFast

#---------------------------------------------------------------------#

# Author: Abhishek Harikrishnan
# Email: abhishek.harikrishnan@fu-berlin.de
# Last updated: 08-12-2023

#---------------------------------------------------------------------#

class vorticityAndStrainTensors:
	
	'''
	Calculation of vorticity (spin) and strain tensors which are skew-
	symmetric and symmetric part of the velocity gradient tensor ∇v i.e., 
	
	∇v = Ω + S
	
	Vorticity (spin) tensor Ω = 0.5 (∇v - ∇v^T)
	Strain rate tensor S = 0.5 (∇v + ∇v^T)
	
	'''
	
	def __init__(self, u, v, w, dx, dy, dz, _dtype):
		
		# First calculate the velocity gradient tensor
		
		self.du =  np.gradient(u, dx, dy, dz)
		self.dv =  np.gradient(v, dx, dy, dz)
		self.dw =  np.gradient(w, dx, dy, dz)
	
	def velocityGradient(self):
		
		# Returns the velocity gradient tensor
		
		return [self.du, self.dv, self.dw]
	
	def vorticityTensor(self):
		
		# Calculate the vorticity tensor
		
		xlen, ylen, zlen = np.shape(self.du[0])
		
		o11 = np.zeros((xlen, ylen, zlen), dtype = self.du[0].dtype)
		o12 = np.multiply((np.subtract(self.du[1],self.dv[0])), 0.5)
		o13 = np.multiply((np.subtract(self.du[2],self.dw[0])), 0.5)

		o21 = np.multiply((np.subtract(self.dv[0],self.du[1])), 0.5)
		o22 = np.zeros((xlen, ylen, zlen), dtype = self.du[0].dtype)
		o23 = np.multiply((np.subtract(self.dv[2],self.dw[1])), 0.5)

		o31 = np.multiply((np.subtract(self.dw[0],self.du[2])), 0.5)
		o32 = np.multiply((np.subtract(self.dw[1],self.dv[2])), 0.5)
		o33 = np.zeros((xlen, ylen, zlen), dtype = self.du[0].dtype)
		
		return [o11, o12, o13, o21, o22, o23, o31, o32, o33]
	
	def strainTensor(self):
		
		# Calculate strain rate tensor
		
		s11 = self.du[0]
		s12 = np.multiply((np.add(self.du[1],self.dv[0])), 0.5)
		s13 = np.multiply((np.add(self.du[2],self.dw[0])), 0.5)

		s21 = np.multiply((np.add(self.dv[0],self.du[1])), 0.5)
		s22 = self.dv[1]
		s23 = np.multiply((np.add(self.dv[2],self.dw[1])), 0.5)

		s31 = np.multiply((np.add(self.dw[0],self.du[2])), 0.5)
		s32 = np.multiply((np.add(self.dw[1],self.dv[2])), 0.5)
		s33 = self.dw[2]
		
		return [s11, s12, s13, s21, s22, s23, s31, s32, s33]


# Trial

# xlen = 256
# ylen = 256
# zlen = 256

# u = array.array('f')
# fr = open('0u.bin', 'rb')
# u.fromfile(fr, (xlen*ylen*zlen))
# fr.close()

# v = array.array('f')
# fr = open('0v.bin', 'rb')
# v.fromfile(fr, (xlen*ylen*zlen))
# fr.close()

# w = array.array('f')
# fr = open('0w.bin', 'rb')
# w.fromfile(fr, (xlen*ylen*zlen))
# fr.close()

# # Set dtype
# _dtype = np.float32

# u = np.reshape(u, [xlen, ylen, zlen])
# v = np.reshape(v, [xlen, ylen, zlen])
# w = np.reshape(w, [xlen, ylen, zlen])

# x = np.linspace(0, 2*np.pi, xlen, dtype = _dtype)
# # y = (1 - np.cos(np.pi * (np.array(range(ylen + 1))) / (len(range(ylen + 1)) - 1)))-1
# y = np.linspace(0, 2*np.pi, ylen, dtype = _dtype)
# z = np.linspace(0, 2*np.pi, zlen, dtype = _dtype)

# dx = x[2] - x[1]
# dy = y[2] - y[1]
# dz = z[2] - z[1]

# # raise SystemError

# velGradientObj = vorticityAndStrainTensors(u, v, w, dx, dy, dz, _dtype)
# velocityGradientTensor = velGradientObj.velocityGradient()
# vorticityTensor = velGradientObj.vorticityTensor()
# strainTensor = velGradientObj.strainTensor()

# # Calculate tensors

# tensorObj = tensorOperationsFast(vorticityTensor)
# vortNorm = tensorObj.calculateEuclideanNorm()

# tensorObj = tensorOperationsFast(strainTensor)
# strainNorm = tensorObj.calculateEuclideanNorm()

# q = 0.5 * (vortNorm**2 - strainNorm**2)

# visObject = mayaviVisualizeWithThreshold(q)
# visObject.configure_traits()

# Sanity check
# qCriterion values do match with vortex extraction

# vorticityMag = vExtractObj.vorticityMagnitude()
# qCrit = vExtractObj.qCriterion()
# deltaCrit = vExtractObj.deltaCriterion()
