# Supplement to Mayavi Visualization
# All playground options are defined here

from traits.api import on_trait_change
import numpy as np
import scipy
from mayavi import mlab

class allPlaygroundOptions:
	
	def get_kGrid(self, N, l, k_min, D, TruncatedGrid = False, k0 = False):
    
		n_k0 = 1 if k0 else 0

		points = np.zeros((2 * N + n_k0,))
		for n in range(N):
			if not l == 1:
				points[N + n + n_k0] = l**n
				points[N - 1 - n] = -(l**n)
			else:
				points[N + n + n_k0] = 1*(n+1)
				points[N - 1 - n] = -(1*(n+1))
		points = np.array(points) * k_min
		print('Points on Grid:', points/k_min)
		
		ks_space = [np.zeros((2 * N + n_k0,) * D)]
		for p in range(len(points)):
			ks_space[0][p] = points[p]
		
		ks_space.extend(np.swapaxes(ks_space[0], 0, i) for i in range(1, D))
		
		if TruncatedGrid:
			ks_space = np.array([ks[N:] for ks in ks_space])
		
		ks_modulus = np.sqrt(np.sum([ks_i**2 for ks_i in ks_space], axis=0))
		
		return np.array(ks_space)/k_min, ks_modulus

	def get_grid_for_plotting(self, gridPts):
		
		s = np.ones_like(gridPts[0]).ravel() # dummy scalar grid
			
		# Scale and plot the grid
		gridPts_x = gridPts[0] / np.max(gridPts[0])
		gridPts_x = gridPts_x * float(self.xmax_LL) # This ensures that data is within the preferred extent
		gridPts_x = gridPts_x.ravel()
		
		gridPts_y = gridPts[1] / np.max(gridPts[0])
		gridPts_y = gridPts_y * float(self.ymax_LL) # This ensures that data is within the preferred extent
		gridPts_y = gridPts_y.ravel()
		
		gridPts_z = gridPts[2] / np.max(gridPts[0])
		gridPts_z = gridPts_z * float(self.zmax_LL) # This ensures that data is within the preferred extent
		gridPts_z = gridPts_z.ravel()
		
		return s, gridPts_x, gridPts_y, gridPts_z
	
	def l_value(self, a, b):
		lv = float(scipy.optimize.fsolve(lambda x: x**b - x**a - 1, np.array(2))[0])
		print('l value:', lv)
		return lv
	
	@on_trait_change('allPlaygroundOptionsActual, seedScale_playground, \
	includeK0_playground, numGridPoints_playground, a_playground, b_playground')
	def allPlaygroundOptionsActualChanged(self):
		
		# Remove stuff if already created
		try:
			self.gridPlot.remove()
			self.gridPlotGlyph.remove()
		except:
			pass
		
		# Show the Fourier grid on which the structures are being generated
		
		# By default, these are 3 dimensional grids
		D = 3
		
		# For now, set k_min = 2*pi
		k_min = 2 * np.pi
		
		# Always generate the full grids
		TruncatedGrid = False
		
		if self.allPlaygroundOptionsActual == 'Linear':
			
			l = 1 # Linearly spaced modes
			gridPts, _ = self.get_kGrid(int(self.numGridPoints_playground), l, k_min, D, TruncatedGrid, self.includeK0_playground)
			
			s, gridPts_x, gridPts_y, gridPts_z = self.get_grid_for_plotting(gridPts)
			
			self.gridPlot = mlab.pipeline.scalar_scatter(gridPts_x, gridPts_y, gridPts_z, s, figure = self.scene1.mayavi_scene)
			self.gridPlotGlyph = mlab.pipeline.glyph(self.gridPlot, scale_mode = 'none', scale_factor = self.seedScale_playground)
		
		elif self.allPlaygroundOptionsActual == 'Logarithmic':
			
			l = self.l_value(self.a_playground, self.b_playground)
			gridPts, _ = self.get_kGrid(int(self.numGridPoints_playground), l, k_min, D, TruncatedGrid, self.includeK0_playground)
			
			s, gridPts_x, gridPts_y, gridPts_z = self.get_grid_for_plotting(gridPts)
			
			self.gridPlot = mlab.pipeline.scalar_scatter(gridPts_x, gridPts_y, gridPts_z, s, figure = self.scene1.mayavi_scene)
			self.gridPlotGlyph = mlab.pipeline.glyph(self.gridPlot, scale_mode = 'none', scale_factor = self.seedScale_playground)
			
			
			
		
	# @on_trait_change('GenerateStructure')
	# def generateStructureChanged(self):
		
		# # TODO - Show dialog box that this will overwrite time series 1
		
		# print(self.initCondition1)
		
		
		
		
