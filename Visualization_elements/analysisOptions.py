# Supplement to Mayavi Visualization
# All analysis options are defined here

from traits.api import on_trait_change
import numpy as np
import mayavi
from mayavi import mlab
import os
import matplotlib.pyplot as plt
from numba import jit

@jit(nopython = True, cache = True)
def calculate_QTensor3D(vortVec, dx, dy, dz):

	Q_tensor = np.zeros((3, 3))
	
	for i in range(len(vortVec)):
		outerMul = np.outer(vortVec[i], vortVec[i])
		dotProd = np.dot(vortVec[i], vortVec[i])
		Q_tensor += outerMul - ((dotProd/3) * np.eye(3))
	
	Q_tensor = Q_tensor * dx * dy * dz
	
	# Calculate eigenvalues and eigenvectors
	eigenvalue, eigenvectors = np.linalg.eigh(Q_tensor)

	return Q_tensor, eigenvectors, eigenvalue

class allAnalysisOptions:	
	
	@on_trait_change('calculateQtensor')
	def calculateQtensorChanged(self):
		
		if self.screen1_ts1:
			
			try:
				if self.quiver_sc1:
					self.quiver_sc1.remove()
			except:
				pass
			
			# Calculate Q-tensor within alternate bounding box if necessary
			
			if self.altBBox:
				xmin_reconn = self.whichSliceX1_reconn
				xmax_reconn = self.whichSliceX2_reconn
				ymin_reconn = self.whichSliceY1_reconn
				ymax_reconn = self.whichSliceY2_reconn
				zmin_reconn = self.whichSliceZ1_reconn
				zmax_reconn = self.whichSliceZ2_reconn
				
				w1 = self.omega1[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, self.whichTime1]
				w2 = self.omega2[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, self.whichTime1]
				w3 = self.omega3[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, self.whichTime1]
			else:
				w1 = self.omega1[:, :, :, self.whichTime1]
				w2 = self.omega2[:, :, :, self.whichTime1]
				w3 = self.omega3[:, :, :, self.whichTime1]
			
			vortVec = np.c_[w1.ravel(), w2.ravel(), w3.ravel()]
			
			QT, EigVec, EigVal = calculate_QTensor3D(vortVec,
			self.dx_data1, self.dy_data1, self.dz_data1)
			
			print(EigVec, EigVal)
			
			# For automatic scale factor, use the dimenion with the smallest length
			allMaxLengths = np.array([np.max(self.x1), np.max(self.y1), np.max(self.z1)])
			
			# plot quiver of EigVecs
			self.quiver_sc1 = mlab.quiver3d([0,0,0],[0,0,0],[0,0,0],EigVec[0],EigVec[1],EigVec[2], scale_factor = np.min(allMaxLengths), figure=self.scene1.mayavi_scene)
			
	
	@on_trait_change('whichSliceX1_reconn, whichSliceY1_reconn, whichSliceZ1_reconn, whichSliceX2_reconn, whichSliceY2_reconn, whichSliceZ2_reconn')
	def bboxChangedReconn(self):
		
		if self.screen1_ts1:
			
			try:
				self.reconn_sc1.remove()
			except:
				pass
			
			xmin = np.unique(self.x1)[self.whichSliceX1_reconn]
			ymin = np.unique(self.y1)[self.whichSliceY1_reconn]
			zmin = np.unique(self.z1)[self.whichSliceZ1_reconn]
			
			xmax = np.unique(self.x1)[self.whichSliceX2_reconn]
			ymax = np.unique(self.y1)[self.whichSliceY2_reconn]
			zmax = np.unique(self.z1)[self.whichSliceZ2_reconn]
			
			if xmax > xmin and ymax > ymin and zmax > zmin:
			
				self.reconn_sc1 = mayavi.tools.pipeline.outline(self.iso1_sc1, 
				color = (1, 0, 0), line_width = 2, opacity = 1, 
				extent = [xmin, xmax, ymin, ymax, zmin, zmax])
	
	@on_trait_change('calcReconnection')
	def calcReconnectionChanged(self):
		
		if self.screen1_ts1:
			
			try:
				self.reconn_sc1.remove()
			except:
				pass
			
			if self.altBBox:
				xmin_reconn = self.whichSliceX1_reconn
				xmax_reconn = self.whichSliceX2_reconn
				ymin_reconn = self.whichSliceY1_reconn
				ymax_reconn = self.whichSliceY2_reconn
				zmin_reconn = self.whichSliceZ1_reconn
				zmax_reconn = self.whichSliceZ2_reconn
			
			# First calculate the time-averaged Q-tensor
			
			# Get total time
			total_time = int(np.shape(self._dataTs1)[-1]-1)
			
			# Fire next time series button
			for i in range(0, total_time):
				
				# Reset self.whichTime1
				self.whichTime1 = i
				
				# Get vorticity
				if self.altBBox:
					w1 = self.omega1[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, self.whichTime1]
					w2 = self.omega2[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, self.whichTime1]
					w3 = self.omega3[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, self.whichTime1]
				else:
					w1 = self.omega1[:, :, :, self.whichTime1]
					w2 = self.omega2[:, :, :, self.whichTime1]
					w3 = self.omega3[:, :, :, self.whichTime1]
				
				print('Q-tensor calc.. processing time step: ' + str(i) + '/' + str(total_time))
				
				vortVec = np.c_[w1.ravel(), w2.ravel(), w3.ravel()]
				
				# Calculate q-tensor and recalculate enstrophy and its components in the new basis
				QT, EigVec, EigVal = calculate_QTensor3D(vortVec, 
				self.dx_data1, self.dy_data1, self.dz_data1)
				
				points = np.c_[w1.ravel(), w2.ravel(), w3.ravel()]
				
				if i == 0:
					
					EigVecSorted = np.zeros((np.shape(EigVec)))
				
				# Sort the eigenvectors with the descending order of eigenvalues
				EigVecSorted += EigVec[np.argsort(EigVal)[::-1]]
			
			EigVecSorted /= total_time
			
			# Calculate enstrophy components for all time (with and without Q-tensor)
			# and plot
			
			E1 = []
			E2 = []
			E3 = []
			ET = []
			
			E1_q = []
			E2_q = []
			E3_q = []
			ET_q = []
			
			# Get total time
			total_time = int(np.shape(self._dataTs1)[-1]-1)
			
			# Fire next time series button
			for i in range(0, total_time):
				
				print('Processing time step: ' + str(i) + '/' + str(total_time))
				
				# Reset self.whichTime1
				self.whichTime1 = i
				
				# Get vorticity
				if self.altBBox:
					w1 = self.omega1[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, self.whichTime1]
					w2 = self.omega2[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, self.whichTime1]
					w3 = self.omega3[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, self.whichTime1]
				else:
					w1 = self.omega1[:, :, :, self.whichTime1]
					w2 = self.omega2[:, :, :, self.whichTime1]
					w3 = self.omega3[:, :, :, self.whichTime1]
				
				# Calculate enstrophy and its components
				E1.append(0.5 * np.sum(w1**2) * self.dx_data1  * self.dy_data1  * self.dz_data1)
				E2.append(0.5 * np.sum(w2**2) * self.dx_data1  * self.dy_data1  * self.dz_data1)
				E3.append(0.5 * np.sum(w3**2) * self.dx_data1  * self.dy_data1  * self.dz_data1)
				ET.append(E1[i] + E2[i] + E3[i])
				
				# Calculate q-tensor and recalculate enstrophy and its components in the new basis
				# QT, EigVec, EigVal = self.calculate_QTensor3D(self.omega1[:, :, :, self.whichTime1], 
				# self.omega2[:, :, :, self.whichTime1], self.omega3[:, :, :, self.whichTime1], 
				# self.dx_data1, self.dy_data1, self.dz_data1, True)
				
				points = np.c_[w1.ravel(), w2.ravel(), w3.ravel()]
				
				# Sort the eigenvectors with the descending order of eigenvalues
				EigVecSorted = EigVec[np.argsort(EigVal)[::-1]]
				
				w_r = points@EigVecSorted
				
				E1_q.append(0.5 * np.sum(w_r[:, 0]**2) * self.dx_data1  * self.dy_data1  * self.dz_data1)
				E2_q.append(0.5 * np.sum(w_r[:, 1]**2) * self.dx_data1  * self.dy_data1  * self.dz_data1)
				E3_q.append(0.5 * np.sum(w_r[:, 2]**2) * self.dx_data1  * self.dy_data1  * self.dz_data1)
				ET_q.append(E1_q[i] + E2_q[i] + E3_q[i])
			
			
			fig, ax = plt.subplots(1, 2)
			ax[0].plot(E1, '--r', linewidth = 0.5, label = 'E1')
			ax[0].plot(E2, '-g', linewidth = 0.5, label = 'E2')
			ax[0].plot(E3, '-b', linewidth = 0.5, label = 'E3')
			ax[0].plot(ET, '-k', linewidth = 1, label = 'ET')
			ax[0].set_title('Without q-tensor')
			ax[0].legend()
			ax[1].plot(E1_q, '--r', linewidth = 0.5, label = 'E1')
			ax[1].plot(E2_q, '-g', linewidth = 0.5, label = 'E2')
			ax[1].plot(E3_q, '-b', linewidth = 0.5, label = 'E3')
			ax[1].plot(ET_q, '-k', linewidth = 1, label = 'ET')
			ax[1].set_title('With q-tensor')
			ax[1].legend()
			plt.show()
			
			
			
		
		
