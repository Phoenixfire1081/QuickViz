# Supplement to Mayavi Visualization
# All playground options are defined here

from traits.api import on_trait_change
import numpy as np
import scipy
from mayavi import mlab
from scipy.spatial.transform import Rotation
from .vortexExtraction import vortexExtract

# Check for cupy
try:
	import cupy as cp
	from .iDFT import inverseDFTcupy as inverseDFT
	from .iDFT import inverseDFTsingleScalarcupy as inverseDFTsingleScalar
except:
	print('Calculation will be done with CPU. GPU recommended. See the CuPy installation page.')
	from .iDFT import inverseDFT
	from .iDFT import inverseDFTsingleScalar

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
	
	def laplacian(self, arr):
		return -arr**2

	def inv(self, f):
		f = np.array(f)
		nz = f != 0
		f[nz] = 1 / f[nz]
		return f

	def laplacian_inv(self, arr):
		return self.inv(self.laplacian(arr))

	def cross3D(self, a, b):
		ax, ay, az = np.array(a)
		bx, by, bz = b
		return np.array([ay * bz - az * by, bx * az - bz * ax, ax * by - ay * bx])

	def rot3D(self, ks, a):
		return 1j * self.cross3D(ks, a)

	def rot3D_inv(self, ks, ks_modulus, a):
		return -self.laplacian_inv(ks_modulus) * self.rot3D(ks, a)
		
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
			gridPts, ks_modulus = self.get_kGrid(int(self.numGridPoints_playground), l, k_min, D, TruncatedGrid, self.includeK0_playground)
			self.gridPts = gridPts
			self.ks_modulus = ks_modulus
		
		elif self.allPlaygroundOptionsActual == 'Logarithmic':
			
			l = self.l_value(self.a_playground, self.b_playground)
			gridPts, ks_modulus = self.get_kGrid(int(self.numGridPoints_playground), l, k_min, D, TruncatedGrid, self.includeK0_playground)
			self.gridPts = gridPts
			self.ks_modulus = ks_modulus
		
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
			
			self.x_playground = points[:, 0] + self.translatex_playground
			self.y_playground = points[:, 1] + self.translatey_playground
			self.z_playground = points[:, 2] + self.translatez_playground
			
			# Plot the object
			self.plottedObject = mlab.plot3d(self.x_playground, self.y_playground, 
			self.z_playground, tube_radius=None, color = (1, 0, 0), 
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
	
	@on_trait_change('GenerateTS_playground')		
	def GenerateTS_playground_fired(self):
		
		# For now overwrite TS2, this should be changed later
		self.nts = 2
		
		# Initialize based on input data
		# self._dataTs2 = np.zeros((3, 3, 3, 1), dtype = np.float32)
		
		x, dx = np.linspace(float(self.xmin_LL), float(self.xmax_LL), int(self.xres_LL), retstep = True)
		y, dy = np.linspace(float(self.ymin_LL), float(self.ymax_LL), int(self.yres_LL), retstep = True)
		z, dz = np.linspace(float(self.zmin_LL), float(self.zmax_LL), int(self.zres_LL), retstep = True)
		
		xx, yy, zz = np.meshgrid(x, y, z, indexing = 'ij')

		xx_i, yy_i, zz_i = np.mgrid[x[0]:x[-1]:len(x)*1j, y[0]:y[-1]:len(y)*1j, z[0]:z[-1]:len(z)*1j]
		
		self.x2 = xx
		self.y2 = yy
		self.z2 = zz
		
		self.dx_data2 = dx
		self.dy_data2 = dy
		self.dz_data2 = dz
		
		self.u2 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), int(self.timeStep_LL)), dtype = np.float32)
		self.v2 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), int(self.timeStep_LL)), dtype = np.float32)
		self.w2 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), int(self.timeStep_LL)), dtype = np.float32)
		self.omega1_2 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), int(self.timeStep_LL)), dtype = np.float32)
		self.omega2_2 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), int(self.timeStep_LL)), dtype = np.float32)
		self.omega3_2 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), int(self.timeStep_LL)), dtype = np.float32)
		self._dataTs2 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), int(self.timeStep_LL)), dtype = np.float32)
		
		self.ts2max = int(self.timeStep_LL)
	
	@on_trait_change('ResetTS_playground')		
	def ResetTS_playground_fired(self):
		
		# For now this is enough. Actually reset it later
		self.nts = 1
		
	@on_trait_change('GenerateStructure')
	def generateStructure_fired(self):
		
		# Works only when Fourier grid type is not None
		# The procedure needs to be updated depending on the structure. 
		# Use actual formulas. This is not accurate. 
		
		if not self.allPlaygroundOptionsActual == 'None':
			
			N_s = 1204           # number of sample points along the line
			s = np.linspace(float(self.xmin_LL), float(self.xmax_LL), N_s)
			dt = s[1] - s[0]
			
			R = np.vstack([self.x_playground, self.y_playground, self.z_playground])  

			# Compute the tangent vector T(t) (using finite differences)
			dR_dt = np.gradient(R, dt, axis=1)
			T = dR_dt / np.linalg.norm(dR_dt, axis=0)  # shape (3, N_t)
			
			kx, ky, kz = self.gridPts
			u0 = np.exp(-((kx*float(self.thickness_playground))**2 + (ky*float(self.thickness_playground))**2 + (kz*float(self.thickness_playground))**2)/2)
			
			w1x = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL)), dtype=complex)
			w1y = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL)), dtype=complex)
			w1z = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL)), dtype=complex)
			
			for i in range(int(self.xres_LL)):
				for j in range(int(self.yres_LL)):
					for k in range(int(self.zres_LL)):
						# Current k-vector
						k_vec = np.array([kx[i,j,k], ky[i,j,k], kz[i,j,k]])
						# Compute phase = k · R(t) for all t; note R has shape (3, N_t)
						# The dot product is: k_vec[0]*X + k_vec[1]*Y + k_vec[2]*Z.
						phase1 = k_vec[0]*self.x_playground + k_vec[1]*self.y_playground + k_vec[2]*self.z_playground  # shape (N_t,)
						exp_factor1 = np.exp(-1j * phase1)  # shape (N_t,)
						# For each vector component, integrate T[comp, t]*exp_factor dt over t.
						w1x[i,j,k] = np.sum(T[0, :] * exp_factor1) * dt * (np.cos(kx[i,j,k] * self.translatex_playground) + 1j * np.sin(kx[i,j,k] * self.translatex_playground)) * (np.cos(ky[i,j,k] * self.translatey_playground) + 1j * np.sin(ky[i,j,k] * self.translatey_playground)) * (np.cos(kz[i,j,k] * self.translatez_playground) + 1j * np.sin(kz[i,j,k] * self.translatez_playground)) 
						w1y[i,j,k] = np.sum(T[1, :] * exp_factor1) * dt * (np.cos(kx[i,j,k] * self.translatex_playground) + 1j * np.sin(kx[i,j,k] * self.translatex_playground)) * (np.cos(ky[i,j,k] * self.translatey_playground) + 1j * np.sin(ky[i,j,k] * self.translatey_playground)) * (np.cos(kz[i,j,k] * self.translatez_playground) + 1j * np.sin(kz[i,j,k] * self.translatez_playground)) 
						w1z[i,j,k] = np.sum(T[2, :] * exp_factor1) * dt * (np.cos(kx[i,j,k] * self.translatex_playground) + 1j * np.sin(kx[i,j,k] * self.translatex_playground)) * (np.cos(ky[i,j,k] * self.translatey_playground) + 1j * np.sin(ky[i,j,k] * self.translatey_playground)) * (np.cos(kz[i,j,k] * self.translatez_playground) + 1j * np.sin(kz[i,j,k] * self.translatez_playground)) 
			
			w1x = w1x * u0
			w1y = w1y * u0
			w1z = w1z * u0
			
			ux, uy, uz = self.rot3D_inv(self.gridPts, self.ks_modulus, [w1x, w1y, w1z])
			
			velx, vely, velz = inverseDFT(int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), 
			kx.ravel(), ky.ravel(), kz.ravel(), self.x2, self.y2, self.z2, 
			ux.ravel(), uy.ravel(), uz.ravel())
			
			# self.omega1_2[:, :, :, self.whichTime2] = w1x * u0
			# self.omega2_2[:, :, :, self.whichTime2] = w1y * u0
			# self.omega3_2[:, :, :, self.whichTime2] = w1z * u0
			
			# self.u2[:, :, :, self.whichTime2], self.v2[:, :, :, self.whichTime2], self.w2[:, :, :, self.whichTime2] = self.rot3D_inv(self.gridPts, self.ks_modulus, [w1x, w1y, w1z])
			self.u2[:, :, :, self.whichTime2] = velx
			self.v2[:, :, :, self.whichTime2] = vely
			self.w2[:, :, :, self.whichTime2] = velz
			
			# Compute vorticity vector and requested scalar
			vortices = vortexExtract(self.u2[:, :, :, self.whichTime2], self.v2[:, :, :, self.whichTime2], self.w2[:, :, :, self.whichTime2], self.dx_data2, self.dy_data2, self.dz_data2)
			vortx, vorty, vortz = vortices.vorticityComponents()
			
			self.omega1_2[:, :, :, self.whichTime2] = vortx
			self.omega2_2[:, :, :, self.whichTime2] = vorty
			self.omega3_2[:, :, :, self.whichTime2] = vortz
			
			self.whichScalar_LL = 'Q-criterion'
			
			if self.whichScalar_LL == 'Vorticity magnitude':
				scalar = vortices.vorticityMagnitude()
			elif self.whichScalar_LL == 'Q-criterion':
				scalar = vortices.qCriterion()
			elif self.whichScalar_LL == 'Lambda_2':
				scalar = vortices.lambda2Criterion()
			elif self.whichScalar_LL == 'Delta criterion':
				scalar = vortices.deltaCriterion()
			elif self.whichScalar_LL == 'Enstrophy density':
				scalar = vortices.enstrophyDensity()
			elif self.whichScalar_LL == 'Enstrophy Prod. Rate':
				scalar = vortices.enstrophyProductionRate()
			
			self._dataTs2[:, :, :, self.whichTime2] = scalar
			
	
	@on_trait_change('removeStructure')
	def removeStructure_fired(self):
		
		# Simply reset the data of TS2, needs to be changed later
		
		self.u2 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), int(self.timeStep_LL)), dtype = np.float32)
		self.v2 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), int(self.timeStep_LL)), dtype = np.float32)
		self.w2 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), int(self.timeStep_LL)), dtype = np.float32)
		self.omega1_2 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), int(self.timeStep_LL)), dtype = np.float32)
		self.omega2_2 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), int(self.timeStep_LL)), dtype = np.float32)
		self.omega3_2 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), int(self.timeStep_LL)), dtype = np.float32)
		self._dataTs2 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), int(self.timeStep_LL)), dtype = np.float32)
		
		
		
		
