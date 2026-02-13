# Supplement to Mayavi Visualization
# All playground options are defined here

from traits.api import on_trait_change
import numpy as np
import scipy
from mayavi import mlab
from scipy.spatial.transform import Rotation

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
	includeK0_playground, numGridPoints_playground, a_playground, b_playground, \
	visualizeGrid_playground')
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
		
		elif self.allPlaygroundOptionsActual == 'Logarithmic':
			
			l = self.l_value(self.a_playground, self.b_playground)
			gridPts, _ = self.get_kGrid(int(self.numGridPoints_playground), l, k_min, D, TruncatedGrid, self.includeK0_playground)
		
		if not self.allPlaygroundOptionsActual == 'None' and self.visualizeGrid_playground: # Only if the user wants to visualize the grid
				
			s, gridPts_x, gridPts_y, gridPts_z = self.get_grid_for_plotting(gridPts)
			
			self.gridPlot = mlab.pipeline.scalar_scatter(gridPts_x, gridPts_y, gridPts_z, s, figure = self.scene1.mayavi_scene)
			self.gridPlotGlyph = mlab.pipeline.glyph(self.gridPlot, scale_mode = 'none', scale_factor = self.seedScale_playground)
			
	@on_trait_change('allPredefinedVortices, rotAxisX_playground,\
	rotAxisY_playground, rotAxisZ_playground, rotationAngle_playground, \
	translatex_playground, translatey_playground, translatez_playground, \
	ringRadius_playground, thickness_playground, allPredefinedKnots,\
	p_torus, q_torus')		
	def allPredefinedVorticesChanged(self):
		
		res = 1000 # Set a default resolution of 100 points. 
		theta = np.linspace(0, 2*np.pi, res) # This is also set by default
		
		# Remove stuff if already created
		try:
			self.plottedObject.parent.parent.remove() # this is to remove the linesource object
			self.plottedObject.remove()
		except:
			pass
		
		# Show a plot of the object
		if self.allPredefinedVortices == 'Vortex ring':
			
			# Plot ring on the XY plane
			x = float(self.ringRadius_playground) * np.cos(theta)
			y = float(self.ringRadius_playground) * np.sin(theta)
			z = np.zeros_like(theta)
		
		elif self.allPredefinedVortices == 'Vortex tube':
			
			# Plot the tube along X
			x = np.linspace(float(self.xmin_LL), float(self.xmax_LL), res)
			y = np.zeros_like(x)
			z = np.zeros_like(x)
		
		elif self.allPredefinedVortices == 'Vortex knot':
			
			if self.allPredefinedKnots == 'Trefoil':

				x = float(self.ringRadius_playground) * (np.sin(theta) + 2 * np.sin(2 * theta))
				y = float(self.ringRadius_playground) * (np.cos(theta) - 2 * np.cos(2 * theta))
				z = float(self.ringRadius_playground) * (- np.sin(3*theta))
			
			elif self.allPredefinedKnots == '(p,q) Torus':
				
				r = np.cos(float(self.q_torus) * theta) + 2
				x = float(self.ringRadius_playground) * (r * np.cos(int(self.p_torus) * theta))
				y = float(self.ringRadius_playground) * (r * np.sin(int(self.p_torus) * theta))
				z = float(self.ringRadius_playground) * (- np.sin(float(self.q_torus) * theta))
			
		
		if not self.allPredefinedVortices == 'None':
		
			# Rotate the object before applying any translation
			rotation_x = Rotation.from_euler('x', self.rotationAngle_playground, degrees=True)
			rotation_y = Rotation.from_euler('y', self.rotationAngle_playground, degrees=True)
			rotation_z = Rotation.from_euler('z', self.rotationAngle_playground, degrees=True)
			
			points = np.vstack((x, y, z)).T
			
			if self.rotAxisX_playground == '1':
				points = rotation_x.apply(points)
			if self.rotAxisY_playground == '1':
				points = rotation_y.apply(points)
			if self.rotAxisZ_playground == '1':
				points = rotation_z.apply(points)
			
			x = points[:, 0]
			y = points[:, 1]
			z = points[:, 2]
			
			# Plot the object
			self.plottedObject = mlab.plot3d(x + self.translatex_playground, y + self.translatey_playground, 
			z + self.translatez_playground, tube_radius=None, color = (1, 0, 0), 
			line_width = float(self.thickness_playground)*30, figure = self.scene1.mayavi_scene)
			
			
			# Get actor and manipulate
			# actor = self.plottedObject.actor.actor
			
			# Change origin for translation
			# actor.origin = [self.translatex_playground, self.translatey_playground, self.translatez_playground]
			
			# Directly manipulate rotation based on axis
			# print(actor.rotate_x )
			
			# print(dir(self.plottedObject))
			# print(dir(self.plottedObject.actor))
			# print(dir(self.plottedObject.actor.actor))
			# print(self.plottedObject.actor.actor.origin)
			
		
	# @on_trait_change('GenerateStructure')
	# def generateStructureChanged(self):
		
		# # TODO - Show dialog box that this will overwrite time series 1
		
		# print(self.initCondition1)
		
		
		
		
