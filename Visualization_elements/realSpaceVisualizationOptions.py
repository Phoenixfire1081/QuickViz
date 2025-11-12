# Supplement to Mayavi Visualization
# All real space visualization options are defined here

from traits.api import on_trait_change
import numpy as np
from .iDFT import inverseDFT
from .vortexExtraction import vortexExtract
try:
	from pyloggrid.LogGrid.DataExplorer import DataExplorer
except:
	print('Log lattice data explorer is necessary to run these computations. Try pip install pyloggrid.')

class allRealSpaceVisualizationOptions:
		
	@on_trait_change('computeLL')
	def computeLL_fired(self):
		
		# TODO - Show dialog box that this will overwrite time series 1
		
		print('Chosen path:', self.LL_path)
		print('Timestep (s):', self.timeStep_LL)
		
		# Load path into data explorer
		dexp = DataExplorer(self.LL_path)
			
		ctr = 0
		
		if '-' in self.timeStep_LL:
			minTs = int(self.timeStep_LL.split('-')[0])
			maxTs = int(self.timeStep_LL.split('-')[1]) + 1
			
		else:
			minTs = int(self.timeStep_LL)
			maxTs = int(self.timeStep_LL) + 1
		
		for ts in range(minTs, maxTs):
	
			# Load the chosen time step
			data, grid = dexp.load_step(ts)
			
			# Get the necessary data
			N = data['N_points'] # Number of points
			k0 = data["k0"] # If k0 mode was used in simulation
			
			# Velocity data
			ux = data['fields']['ux']
			uy = data['fields']['uy']
			uz = data['fields']['uz']
			
			# Actual time
			t = data["t"]
			
			# Get k-grid
			kx, ky, kz = grid.ks
			
			# Since simulation is run with N x 2N x 2N modes, build back the velocity
			# fields and k-grid to 2N x 2N x 2N.
			
			# Strictly speaking, this is unnecessary. However, it was noted multiple times
			# that building this back aids with visualization. 
			
			if k0.all():
				UX = np.zeros((2*N+1,2*N+1,2*N+1),dtype=complex)
				UY = np.zeros((2*N+1,2*N+1,2*N+1),dtype=complex)
				UZ = np.zeros((2*N+1,2*N+1,2*N+1),dtype=complex)
				UX[N:,:,:] = ux
				UY[N:,:,:] = uy
				UZ[N:,:,:] = uz
				UX[:N+1,:,:] = ux[::-1, ::-1, ::-1].conjugate()
				UY[:N+1,:,:] = uy[::-1, ::-1, ::-1].conjugate()
				UZ[:N+1,:,:] = uz[::-1, ::-1, ::-1].conjugate()
				UX = (UX+UX[::-1, ::-1, ::-1].conjugate())/2
				UY = (UY+UY[::-1, ::-1, ::-1].conjugate())/2
				UZ = (UZ+UZ[::-1, ::-1, ::-1].conjugate())/2
				KX = np.zeros((2*N+1,2*N+1,2*N+1),dtype=float)
				KY = np.zeros((2*N+1,2*N+1,2*N+1),dtype=float)
				KZ = np.zeros((2*N+1,2*N+1,2*N+1),dtype=float)
				print(np.shape(kx), np.shape(KX))
				KX[N:,:,:] = kx
				KY[N:,:,:] = ky
				KZ[N:,:,:] = kz
				KX[:N+1,:,:] = -kx[::-1,:,:]
				KY[:N+1,:,:] = ky[::-1,:,:]
				KZ[:N+1,:,:] = kz[::-1,:,:]
				
				ux = UX
				uy = UY
				uz = UZ
				kx = KX
				ky = KY
				kz = KZ
			
			else:
				
				UX = np.zeros((2*N,2*N,2*N),dtype=complex)
				UY = np.zeros((2*N,2*N,2*N),dtype=complex)
				UZ = np.zeros((2*N,2*N,2*N),dtype=complex)
				UX[N:,:,:] = ux
				UY[N:,:,:] = uy
				UZ[N:,:,:] = uz
				UX[:N,:,:] = ux[::-1, ::-1, ::-1].conjugate()
				UY[:N,:,:] = uy[::-1, ::-1, ::-1].conjugate()
				UZ[:N,:,:] = uz[::-1, ::-1, ::-1].conjugate()
				UX = (UX+UX[::-1, ::-1, ::-1].conjugate())/2
				UY = (UY+UY[::-1, ::-1, ::-1].conjugate())/2
				UZ = (UZ+UZ[::-1, ::-1, ::-1].conjugate())/2
				KX = np.zeros((2*N,2*N,2*N),dtype=float)
				KY = np.zeros((2*N,2*N,2*N),dtype=float)
				KZ = np.zeros((2*N,2*N,2*N),dtype=float)
				KX[N:,:,:] = kx
				KY[N:,:,:] = ky
				KZ[N:,:,:] = kz
				KX[:N,:,:] = -kx[::-1,:,:]
				KY[:N,:,:] = ky[::-1,:,:]
				KZ[:N,:,:] = kz[::-1,:,:]
				
				ux = UX
				uy = UY
				uz = UZ
				kx = KX
				ky = KY
				kz = KZ
			
			# Build real-space grid
			x, dx = np.linspace(float(self.xmin_LL), float(self.xmax_LL), int(self.xres_LL), retstep = True)
			y, dy = np.linspace(float(self.ymin_LL), float(self.ymax_LL), int(self.yres_LL), retstep = True)
			z, dz = np.linspace(float(self.zmin_LL), float(self.zmax_LL), int(self.zres_LL), retstep = True)
			
			xx, yy, zz = np.meshgrid(x, y, z, indexing = 'ij')
			
			# Compute inverse DFT
			velx, vely, velz = inverseDFT(int(self.xres_LL), int(self.yres_LL), 
			int(self.zres_LL), kx.ravel(), ky.ravel(), kz.ravel(), xx, yy, zz, 
			ux.ravel(), uy.ravel(), uz.ravel())
			
			# Compute vorticity vector and requested scalar
			vortices = vortexExtract(velx, vely, velz, dx, dy, dz)
			vortx, vorty, vortz = vortices.vorticityComponents()
			
			# 'Vorticity magnitude', 'Q-criterion', 'Lambda_2', 'Delta criterion', 'Enstrophy density', 'Enstrophy Prod. Rate'
			
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
			
			# Assign data to time series 1. TODO - Backup if TS already exists.
			
			self.u1[:, :, :, ctr] = velx
			self.v1[:, :, :, ctr] = vely
			self.w1[:, :, :, ctr] = velz
			self.omega1[:, :, :, ctr] = vortx
			self.omega2[:, :, :, ctr] = vorty
			self.omega3[:, :, :, ctr] = vortz
			self._dataTs1[:, :, :, ctr] = scalar
			
			ctr += 1
			
			print('Done')
		
		
