# Supplement to Mayavi Visualization
# All analysis options are defined here

from traits.api import on_trait_change
import numpy as np
from mayavi import mlab
import os

class allAnalysisOptions:	
	
	def calculate_QTensor3D(self, w1, w2, w3, dx, dy, dz, returnEig = False):
    
		vortVec = np.c_[w1.ravel(), w2.ravel(), w3.ravel()]
		Q_tensor = np.zeros((3, 3))
		
		for i in range(len(vortVec)):
			outerMul = np.outer(vortVec[i], vortVec[i])
			dotProd = np.dot(vortVec[i], vortVec[i])
			Q_tensor += outerMul - ((dotProd/3) * np.eye(3))
		
		Q_tensor = Q_tensor * dx * dy * dz
		
		# Calculate eigenvalues and eigenvectors
		eigenvalue, eigenvectors = np.linalg.eigh(Q_tensor)

		if not returnEig:
			return Q_tensor, eigenvectors
		else:
			return Q_tensor, eigenvectors, eigenvalue

	@on_trait_change('calculateQtensor')
	def calculateQtensorChanged(self):
		
		if self.screen1_ts1:
			
			try:
				if self.quiver_sc1:
					self.quiver_sc1.remove()
			except:
				pass
			
			QT, EigVec, EigVal = self.calculate_QTensor3D(self.omega1[:, :, :, self.whichTime1], 
			self.omega2[:, :, :, self.whichTime1], self.omega3[:, :, :, self.whichTime1], 
			self.dx_data1, self.dy_data1, self.dz_data1, True)
			
			print(EigVec, EigVal)
			
			# plot quiver of EigVecs
			self.quiver_sc1 = mlab.quiver3d([0,0,0],[0,0,0],[0,0,0],EigVec[0],EigVec[1],EigVec[2], scale_factor = 0.5, figure=self.scene1.mayavi_scene)
		
		
