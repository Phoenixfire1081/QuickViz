# Supplement to Mayavi Visualization
# All real space visualization options are defined here

from traits.api import on_trait_change
import numpy as np
from scipy.interpolate import RegularGridInterpolator
from .vortexExtraction import vortexExtract
from ..Core_elements.tKinter import folderBrowser
try:
	from pyloggrid.LogGrid.DataExplorer import DataExplorer
except:
	print('Log lattice data explorer is necessary to run these computations. Try pip install pyloggrid.')

# Check for cupy
try:
	import cupy as cp
	from .iDFT import inverseDFTcupy as inverseDFT
	from .iDFT import inverseDFTsingleScalarcupy as inverseDFTsingleScalar
except:
	print('Calculation will be done with CPU. GPU recommended. See the CuPy installation page.')
	from .iDFT import inverseDFT
	from .iDFT import inverseDFTsingleScalar

class allRealSpaceVisualizationOptions:
	
	@on_trait_change('choose_folder_LLPath')
	def choose_folder_LLPath_fired(self):
		
		self.LL_path = folderBrowser()
	
	def build_full_grid(self, scalarField, N, k0):
		
		if k0:
			gridSize = N+1
			res = 2*N+1
		else:
			gridSize = N
			res = 2*N
		
		scalar = np.zeros((res, res, res),dtype=complex)
		scalar[N:,:,:] = scalarField
		scalar[:gridSize,:,:] = scalarField[::-1, ::-1, ::-1].conjugate()
		scalar = (scalar+scalar[::-1, ::-1, ::-1].conjugate())/2
		
		return scalar
	
	def build_full_grid_kmodes(self, kx, ky, kz, N, k0):
		
		if k0:
			gridSize = N+1
			res = 2*N+1
		else:
			gridSize = N
			res = 2*N
		
		KX = np.zeros((res, res, res),dtype=complex)
		KY = np.zeros((res, res, res),dtype=complex)
		KZ = np.zeros((res, res, res),dtype=complex)
		
		KX[N:,:,:] = kx
		KY[N:,:,:] = ky
		KZ[N:,:,:] = kz
		
		KX[:gridSize,:,:] = -kx[::-1,:,:]
		KY[:gridSize,:,:] = ky[::-1,:,:]
		KZ[:gridSize,:,:] = kz[::-1,:,:]
		
		return KX, KY, KZ
	
	def get_sampling_points(self, l_value, N):
		
		if self.samplingPoints_LL == 'Linear':
			
			x, dx = np.linspace(float(self.xmin_LL), float(self.xmax_LL), int(self.xres_LL), retstep = True)
			y, dy = np.linspace(float(self.ymin_LL), float(self.ymax_LL), int(self.yres_LL), retstep = True)
			z, dz = np.linspace(float(self.zmin_LL), float(self.zmax_LL), int(self.zres_LL), retstep = True)
			
			xx, yy, zz = np.meshgrid(x, y, z, indexing = 'ij')
		
		else:
			
			# Use logarithmic sampling points which mimics the Fourier grid
			starting_value = 1/l_value**N
			x = [starting_value]
			for _ in range(N-1):
				x.append((l_value*x[-1])%1)
			pts = np.sort(x)
			
			# Keep all points, even if they fall outside of the requested domain.
			# This will ensure that the RegularGridInterpolator won't throw
			# a out of bounds error
			x = np.unique([-i for i in pts] + [0] + [i for i in pts])
			y = np.unique([-i for i in pts] + [0] + [i for i in pts])
			z = np.unique([-i for i in pts] + [0] + [i for i in pts])
			
			dx = np.gradient(x)
			dy = np.gradient(y)
			dz = np.gradient(z)
			
			xx, yy, zz = np.meshgrid(x, y, z, indexing = 'ij')
			
		return x, y, z, dx, dy, dz, xx, yy, zz
		
	@on_trait_change('computeLL')
	def computeLL_fired(self):
		
		# TODO - Show dialog box that this will overwrite time series 1
		
		print('Chosen path:', self.LL_path)
		print('Timestep (s):', self.timeStep_LL)
		
		# Load path into data explorer
		dexp = DataExplorer(self.LL_path)
			
		if '-' in self.timeStep_LL:
			minTs = int(self.timeStep_LL.split('-')[0])
			maxTs = int(self.timeStep_LL.split('-')[1]) + 1
			
			# Check if skip values are provided
			try: 
				skipTs = int(self.timeStep_LL.split('-')[2])
			except:
				skipTs = 1
			
		else:
			minTs = int(self.timeStep_LL)
			maxTs = int(self.timeStep_LL) + 1
			skipTs = 1
			
		# Completely replace TS1 with new data
		
		self.u1 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), (maxTs - minTs)//skipTs), dtype = np.float32)
		self.v1 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), (maxTs - minTs)//skipTs), dtype = np.float32)
		self.w1 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), (maxTs - minTs)//skipTs), dtype = np.float32)
		self.omega1 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), (maxTs - minTs)//skipTs), dtype = np.float32)
		self.omega2 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), (maxTs - minTs)//skipTs), dtype = np.float32)
		self.omega3 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), (maxTs - minTs)//skipTs), dtype = np.float32)
		self._dataTs1 = np.zeros((int(self.xres_LL), int(self.yres_LL), int(self.zres_LL), (maxTs - minTs)//skipTs), dtype = np.float32)
		
		self.ts1max = (maxTs - minTs)//skipTs - 1 # This updates the slider
		
		# Initialize counter
		ctr = 0
		
		for ts in range(minTs, maxTs, skipTs):
	
			# Load the chosen time step
			data, grid = dexp.load_step(ts)
			
			# Get the necessary data
			N = data['N_points'] # Number of points
			k0 = data["k0"] # If k0 mode was used in simulation
			
			# Actual time
			t = data["t"]
			
			# Get k-grid
			kx, ky, kz = grid.ks
			
			# Velocity data
			ux = data['fields']['ux']
			uy = data['fields']['uy']
			uz = data['fields']['uz']
			try: # If temperature data exists, get it
				temp = data['fields']['theta']
				tempExists = True
			except:
				print('Check other scalar fields that can be plotted:', data['fields'].keys())
				tempExists = False
			
			# Since simulation is run with N x 2N x 2N modes, build back the velocity
			# fields and k-grid to 2N x 2N x 2N.
			
			# Strictly speaking, this is unnecessary. However, it was noted multiple times
			# that building this back aids with visualization. 
			
			ux = self.build_full_grid(ux, N, k0.all())
			uy = self.build_full_grid(uy, N, k0.all())
			uz = self.build_full_grid(uz, N, k0.all())
			
			kx, ky, kz = self.build_full_grid_kmodes(kx, ky, kz, N, k0.all())
			
			if tempExists:
				temperature = self.build_full_grid(temp, N, k0.all())
			
			# Apply filters if chosen
			if self.filterOptions_LL == 'Low-pass':
				
				firstModes = int(self.numModesLP)

				xresmin = N - firstModes + 1
				xresmax = N + firstModes
				
				kx = kx[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax]
				ky = ky[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax]
				kz = kz[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax]

				ux = ux[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax]
				uy = uy[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax]
				uz = uz[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax]
			
			elif self.filterOptions_LL == 'Band-pass':
				
				startVal = int(self.numModesMinBP)
				endVal = int(self.numModesMaxBP)
				
				# Use endVal to slice the grid similar to low pass
				
				xresmin = N - endVal + 1
				xresmax = N + endVal
				
				kx = kx[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax]
				ky = ky[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax]
				kz = kz[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax]

				ux = ux[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax]
				uy = uy[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax]
				uz = uz[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax]
				
				# Now, zero out the mid-velocity values
				
				xresmin = N - startVal + 1
				xresmax = N + startVal
				
				ux[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax] = complex(0)
				uy[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax] = complex(0)
				uz[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax] = complex(0)
			
			elif self.filterOptions_LL == 'High-pass':
				
				lastModes = int(self.numModesHP)
				
				# Now, zero out the mid-velocity values
				
				xresmin = N - lastModes + 1
				xresmax = N + lastModes
				
				ux[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax] = complex(0)
				uy[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax] = complex(0)
				uz[xresmin:xresmax, xresmin:xresmax, xresmin:xresmax] = complex(0)
			
			elif self.filterOptions_LL == 'Gaussian':
				
				# Get magnitude
				ks = np.sqrt(kx**2 + ky**2 + kz**2)
				
				radius = float(self.gaussianSize)
				
				ux = ux * radius * np.exp(-(radius*ks)**2)
				uy = uy * radius * np.exp(-(radius*ks)**2)
				uz = uz * radius * np.exp(-(radius*ks)**2)
			
			# Get the required sampling points based on whether the grid is
			# linearly spaced or logarithmic
			x, y, z, dx, dy, dz, xx, yy, zz = self.get_sampling_points(grid.l, N)
			
			# Compute inverse DFT
			velx, vely, velz = inverseDFT(len(x), len(y), len(z), 
			kx.ravel(), ky.ravel(), kz.ravel(), xx, yy, zz, 
			ux.ravel(), uy.ravel(), uz.ravel())
			
			if tempExists:
				temperature = inverseDFTsingleScalar(len(x), len(y), len(z), 
				kx.ravel(), ky.ravel(), kz.ravel(), xx, yy, zz, 
				temperature.ravel())
			else:
				temperature = np.zeros(np.shape(xx))
			
			# If logarithmic sampling points are used, interpolate onto 
			# a regularly spaced grid for final visualization
			
			if self.samplingPoints_LL == 'Logarithmic':
				
				interpx = RegularGridInterpolator((x, y, z), velx)
				interpy = RegularGridInterpolator((x, y, z), vely)
				interpz = RegularGridInterpolator((x, y, z), velz)
				
				x, dx = np.linspace(float(self.xmin_LL), float(self.xmax_LL), int(self.xres_LL), retstep = True)
				y, dy = np.linspace(float(self.ymin_LL), float(self.ymax_LL), int(self.yres_LL), retstep = True)
				z, dz = np.linspace(float(self.zmin_LL), float(self.zmax_LL), int(self.zres_LL), retstep = True)
				
				xx, yy, zz = np.meshgrid(x, y, z, indexing = 'ij')

				xx_i, yy_i, zz_i = np.mgrid[x[0]:x[-1]:len(x)*1j, y[0]:y[-1]:len(y)*1j, z[0]:z[-1]:len(z)*1j]
				
				velx_i = interpx(np.c_[xx_i.ravel(), yy_i.ravel(), zz_i.ravel()])
				vely_i = interpy(np.c_[xx_i.ravel(), yy_i.ravel(), zz_i.ravel()])
				velz_i = interpz(np.c_[xx_i.ravel(), yy_i.ravel(), zz_i.ravel()])
				
				velx_i = np.reshape(velx_i, np.shape(xx_i))
				vely_i = np.reshape(vely_i, np.shape(xx_i))
				velz_i = np.reshape(velz_i, np.shape(xx_i))
				
				velx = np.float32(velx_i)
				vely = np.float32(vely_i)
				velz = np.float32(velz_i)
				
			# Compute vorticity vector and requested scalar
			vortices = vortexExtract(velx, vely, velz, dx, dy, dz)
			vortx, vorty, vortz = vortices.vorticityComponents()
			
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
			elif self.whichScalar_LL == 'Temperature':
				scalar = temperature
			
			# Assign data to time series 1. TODO - Backup if TS already exists.
			
			self.u1[:, :, :, ctr] = velx
			self.v1[:, :, :, ctr] = vely
			self.w1[:, :, :, ctr] = velz
			self.omega1[:, :, :, ctr] = vortx
			self.omega2[:, :, :, ctr] = vorty
			self.omega3[:, :, :, ctr] = vortz
			self._dataTs1[:, :, :, ctr] = scalar
			
			ctr += 1
		
		# Update x, y, z data as well. Necessary if the visualization was
		# performed for different resolution
		
		self.x1 = xx
		self.y1 = yy
		self.z1 = zz
			
		# Choose the last time step to force refresh
		# Doesn't work when only one time step is calculated
		self.whichTime1 = (maxTs-minTs)//skipTs - 1
		
		
