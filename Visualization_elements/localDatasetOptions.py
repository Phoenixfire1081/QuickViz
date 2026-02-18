# Supplement to QuickViz
# All local dataset options are defined here

from traits.api import on_trait_change
import numpy as np
from .vortexExtraction import vortexExtract
from ..Core_elements.tKinter import folderBrowser
import os
import array
import netCDF4 as nc
import re
import mayavi
from mayavi import mlab

class allLocalDatasetOptions:
	
	@on_trait_change('cancel_LocalData')
	def cancel_LocalData_fired(self):
		
		try: # only if backup data exists
			
			# Restore original data
			self.x1 = self.x1_bk
			self.y1 = self.y1_bk
			self.z1 = self.z1_bk
			
			# Remove modified data
			self.out1_sc1.remove()
			self.sf1_sc1.remove()
			self.iso1_sc1.remove()
			
			self.sf1_sc1 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, self._dataTs1[:, :, :, self.whichTime1], figure=self.scene1.mayavi_scene)
			self.iso1_sc1 = mlab.pipeline.iso_surface(self.sf1_sc1, contours=[self._dataTs1[:, :, :, self.whichTime1].min()])
			
			# Outline will be added automatically
			
		except:
			
			pass # Nothing to do
			
	
	@on_trait_change('choose_folder_LocalDataPath')
	def choose_folder_LocalDataPath_fired(self):
		
		# TODO - a reset feature, where if the user decides not to load data, the original data is restored, done
		
		if self.LocalData_path == os.getcwd():
		
			self.LocalData_path = folderBrowser()
		
		else:
		
			# Update min, max, res data if howToRead.txt is present
				
			fname = '/howToRead.txt'
			if os.path.isfile(self.LocalData_path + fname):
				print('File exists')
				
				# Get bbox data
				print(np.loadtxt(self.LocalData_path + fname, skiprows = 2, max_rows = 1, delimiter = ' '))
				self.xmin_Local, self.xmax_Local, self.ymin_Local, self.ymax_Local, self.zmin_Local, self.zmax_Local = np.loadtxt(self.LocalData_path + fname, skiprows = 2, max_rows = 1, delimiter = ' ', dtype = str)
				
				# Get res data
				self.xres_Local, self.yres_Local, self.zres_Local = np.loadtxt(self.LocalData_path + fname, skiprows = 5, max_rows = 1, delimiter = ' ', dtype = str)
				
				self.howToRead = True
			
			else:
				
				self.howToRead = False
			
			if self.allLocalDatasetOptions == 'Raw 3D':
			
				# Get time step data (calculate from velocity folder)
				self.timeSteps_LocalData = str(len(os.listdir(self.LocalData_path + '/velComp/'))//3)
			
			elif self.allLocalDatasetOptions == 'netCDF': # For netCDF data
				
				# Filter fileList to exclude string only filenames
				self.fileList = os.listdir(self.LocalData_path)
				self.fileList = [i for i in self.fileList if any(char.isdigit() for char in i)]
				
				# Sort data by extracting numbers from string
				self.fileList.sort(key = lambda x: int(re.findall(r'\d+', x)[-1]))
				
				# Update timesteps
				self.timeSteps_LocalData = str(len(self.fileList))
				
				# Open the first file, assign attributes for velocity and list all attributes as well. 
				data = nc.Dataset(self.LocalData_path + '/' + self.fileList[0])
				attribList = list(data.variables.keys())
				
				# Assign velocity labels only if they exist
				
				try:
				
					self.velxLabel = [i for i in attribList if 'v' in i and 'x' in i][0]
					self.velyLabel = [i for i in attribList if 'v' in i and 'y' in i][1]
					self.velzLabel = [i for i in attribList if 'v' in i and 'z' in i][0]
				
				except IndexError:
					
					pass
				
				self.allAttributes = ', '.join(list(data.variables.keys()))
				
				# print('shape:', np.shape(data[attribList[0]][:]))
		
		try:
			# Remove and update BBox
			self.iso1_sc1.remove()
			self.sf1_sc1.remove()
			self.out1_sc1.remove()
		except:
			pass
		
		# Create a temp dataset to get the correct bounding box
		print(self.xres_Local, self.yres_Local, self.zres_Local)
		tmpData = np.zeros((int(self.xres_Local), int(self.yres_Local), int(self.zres_Local)), dtype = np.float32)
		
		x, dx = np.linspace(float(self.xmin_Local), float(self.xmax_Local), int(self.xres_Local), retstep = True)
		y, dy = np.linspace(float(self.ymin_Local), float(self.ymax_Local), int(self.yres_Local), retstep = True)
		z, dz = np.linspace(float(self.zmin_Local), float(self.zmax_Local), int(self.zres_Local), retstep = True)
		
		# Set dx, dy, dz
		self.dx_Local = str(dx)
		self.dy_Local = str(dy)
		self.dz_Local = str(dz)
		
		xx, yy, zz = np.meshgrid(x, y, z, indexing = 'ij')
		
		# Take a backup
		self.x1_bk = self.x1
		self.y1_bk = self.y1
		self.z1_bk = self.z1
		
		self.x1 = xx
		self.y1 = yy
		self.z1 = zz
		
		self.sf1_sc1 = mlab.pipeline.scalar_field(xx, yy, zz, tmpData, figure=self.scene1.mayavi_scene)
		self.iso1_sc1 = mlab.pipeline.iso_surface(self.sf1_sc1, contours=[0])
		
		self.out1_sc1 = mayavi.tools.pipeline.outline(self.iso1_sc1, 
				color = (0, 0, 1), line_width = 2, opacity = 1, 
				extent = [float(self.xmin_Local), float(self.xmax_Local), float(self.ymin_Local), float(self.ymax_Local), float(self.zmin_Local), float(self.zmax_Local)])
		
		# Update max vals for BBox manipulation
		self.maxx1 = int(self.xres_Local)-1
		self.maxy1 = int(self.yres_Local)-1
		self.maxz1 = int(self.zres_Local)-1
			
	@on_trait_change('load_LocalData')
	def load_LocalData_fired(self):
		
		# TODO - this can be combined with real space visualization
		# TODO - import with specific timesteps, similar to real space visualization, done
		# TODO - store specific scalar data?
		
		# If timestep is empty, do not load data
		
		if not self.timeStep_LocalData == '':
		
			# If howToRead doesn't exist, attempt to write to folder
			
			if not self.howToRead:
				
				try:
			
					fw = open(self.LocalData_path + '/howToRead.txt', 'w+')
					fw.write('Bounding Box:\n')
					fw.write('xmin xmax ymin ymax zmin zmax\n')
					fw.write(self.xmin_Local + ' ' + self.xmax_Local + ' ' + self.ymin_Local + ' ' + self.ymax_Local + ' ' + self.zmin_Local + ' ' + self.zmax_Local + '\n')
					fw.write('Resolution:\n')
					fw.write('xres yres zres\n')
					fw.write(self.xres_Local + ' ' + self.yres_Local + ' ' + self.zres_Local + '\n')
					fw.write('Time steps:\n')
					fw.write('minTs maxTs\n')
					fw.write(str(1) + ' ' + str(self.timeSteps_LocalData))
					fw.close()
				
				except PermissionError:
					
					print('Cannot write to folder. Ensure correct permissions..')
			
			if '-' in self.timeStep_LocalData:
				minTs = int(self.timeStep_LocalData.split('-')[0])
				maxTs = int(self.timeStep_LocalData.split('-')[1]) + 1
				
				# Check if skip values are provided
				try: 
					skipTs = int(self.timeStep_LocalData.split('-')[2])
				except:
					skipTs = 1
				
			else:
				minTs = int(self.timeStep_LocalData)
				maxTs = int(self.timeStep_LocalData) + 1
				skipTs = 1
				
				print(minTs, maxTs, skipTs)
			
			# Completely replace TS1 with new data
			
			if self.altBBox:
				xres_alt = self.whichSliceX2_reconn - self.whichSliceX1_reconn
				yres_alt = self.whichSliceY2_reconn - self.whichSliceY1_reconn
				zres_alt = self.whichSliceZ2_reconn - self.whichSliceZ1_reconn
				
				xmin_reconn = self.whichSliceX1_reconn
				xmax_reconn = self.whichSliceX2_reconn
				ymin_reconn = self.whichSliceY1_reconn
				ymax_reconn = self.whichSliceY2_reconn
				zmin_reconn = self.whichSliceZ1_reconn
				zmax_reconn = self.whichSliceZ2_reconn
				
				self.u1 = np.zeros((xres_alt, yres_alt, zres_alt, (maxTs - minTs)//skipTs), dtype = np.float32)
				self.v1 = np.zeros((xres_alt, yres_alt, zres_alt, (maxTs - minTs)//skipTs), dtype = np.float32)
				self.w1 = np.zeros((xres_alt, yres_alt, zres_alt, (maxTs - minTs)//skipTs), dtype = np.float32)
				self.omega1 = np.zeros((xres_alt, yres_alt, zres_alt, (maxTs - minTs)//skipTs), dtype = np.float32)
				self.omega2 = np.zeros((xres_alt, yres_alt, zres_alt, (maxTs - minTs)//skipTs), dtype = np.float32)
				self.omega3 = np.zeros((xres_alt, yres_alt, zres_alt, (maxTs - minTs)//skipTs), dtype = np.float32)
				self._dataTs1 = np.zeros((xres_alt, yres_alt, zres_alt, (maxTs - minTs)//skipTs), dtype = np.float32)
			else:
				self.u1 = np.zeros((int(self.xres_Local), int(self.yres_Local), int(self.zres_Local), (maxTs - minTs)//skipTs), dtype = np.float32)
				self.v1 = np.zeros((int(self.xres_Local), int(self.yres_Local), int(self.zres_Local), (maxTs - minTs)//skipTs), dtype = np.float32)
				self.w1 = np.zeros((int(self.xres_Local), int(self.yres_Local), int(self.zres_Local), (maxTs - minTs)//skipTs), dtype = np.float32)
				self.omega1 = np.zeros((int(self.xres_Local), int(self.yres_Local), int(self.zres_Local), (maxTs - minTs)//skipTs), dtype = np.float32)
				self.omega2 = np.zeros((int(self.xres_Local), int(self.yres_Local), int(self.zres_Local), (maxTs - minTs)//skipTs), dtype = np.float32)
				self.omega3 = np.zeros((int(self.xres_Local), int(self.yres_Local), int(self.zres_Local), (maxTs - minTs)//skipTs), dtype = np.float32)
				self._dataTs1 = np.zeros((int(self.xres_Local), int(self.yres_Local), int(self.zres_Local), (maxTs - minTs)//skipTs), dtype = np.float32)
			
			self.ts1max = (maxTs - minTs)//skipTs - 1 # This updates the slider
			
			if self.precision_LocalData == 'Single':
				_dtype = 'f'
			if self.precision_LocalData == 'Double':
				_dtype = 'd'
			
			DataRes = int(self.xres_Local) * int(self.yres_Local) * int(self.zres_Local)
			
			x, dx = np.linspace(float(self.xmin_Local), float(self.xmax_Local), int(self.xres_Local), retstep = True)
			y, dy = np.linspace(float(self.ymin_Local), float(self.ymax_Local), int(self.yres_Local), retstep = True)
			z, dz = np.linspace(float(self.zmin_Local), float(self.zmax_Local), int(self.zres_Local), retstep = True)
			
			xx, yy, zz = np.meshgrid(x, y, z, indexing = 'ij')
			
			if self.altBBox:
				xx = xx[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn]
				yy = yy[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn]
				zz = zz[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn]
			
			# Initialize counters
			ctr = 0
			fileCtr = minTs
			
			if self.allLocalDatasetOptions == 'Raw 3D':
			
				# Get file list
				flist = os.listdir(self.LocalData_path + '/velComp/')
				flist_x = [i for i in flist if 'velx' in i]
				flist_y = [i for i in flist if 'vely' in i]
				flist_z = [i for i in flist if 'velz' in i]
				flist_x.sort(key = lambda x:int(x.split('_')[1].split('.')[0]))
				flist_y.sort(key = lambda x:int(x.split('_')[1].split('.')[0]))
				flist_z.sort(key = lambda x:int(x.split('_')[1].split('.')[0]))
			
			for ts in range(minTs, maxTs, skipTs):
				
				if self.allLocalDatasetOptions == 'Raw 3D':
					
					# Use array.array to dump velocity data into memory
					# For now, force data as single precision. TODO - support double precision data
					
					velx = array.array(_dtype)
					vely = array.array(_dtype)
					velz = array.array(_dtype)
					
					velx.fromfile(open(self.LocalData_path + '/velComp/' + flist_x[fileCtr], 'rb'), (DataRes))
					vely.fromfile(open(self.LocalData_path + '/velComp/' + flist_y[fileCtr], 'rb'), (DataRes))
					velz.fromfile(open(self.LocalData_path + '/velComp/' + flist_z[fileCtr], 'rb'), (DataRes))
					
					velx = np.reshape(velx, [int(self.xres_Local), int(self.yres_Local), int(self.zres_Local)])
					vely = np.reshape(vely, [int(self.xres_Local), int(self.yres_Local), int(self.zres_Local)])
					velz = np.reshape(velz, [int(self.xres_Local), int(self.yres_Local), int(self.zres_Local)])
				
				elif self.allLocalDatasetOptions == 'netCDF': # For netCDF data
					
					print('Processing:', self.LocalData_path + '/' + self.fileList[fileCtr])
					
					data = nc.Dataset(self.LocalData_path + '/' + self.fileList[fileCtr])
					velx = np.asarray(np.float32(data[self.velxLabel][:]))
					vely = np.asarray(np.float32(data[self.velyLabel][:]))
					velz = np.asarray(np.float32(data[self.velzLabel][:]))
					
					# For delta-omega
					# velx = velx[:, :, :, 0]
					# vely = vely[:, :, :, 0]
					# velz = velz[:, :, :, 0]
					# velx = np.transpose(velx, (1, 0, 2))
					# vely = np.transpose(vely, (1, 0, 2))
					# velz = np.transpose(velz, (1, 0, 2))
				
				if self.altBBox:
					velx = velx[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn]
					vely = vely[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn]
					velz = velz[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn]
					
				# Compute vorticity vector and requested scalar
				vortices = vortexExtract(velx, vely, velz, dx, dy, dz)
				vortx, vorty, vortz = vortices.vorticityComponents()
				
				if self.whichScalar_LocalData == 'Velocity magnitude':
					scalar = vortices.velocityMagnitude()
				elif self.whichScalar_LocalData == 'Vorticity magnitude':
					scalar = vortices.vorticityMagnitude()
				elif self.whichScalar_LocalData == 'Q-criterion':
					scalar = vortices.qCriterion()
				elif self.whichScalar_LocalData == 'Lambda_2':
					scalar = vortices.lambda2Criterion()
				elif self.whichScalar_LocalData == 'Delta criterion':
					scalar = vortices.deltaCriterion()
				elif self.whichScalar_LocalData == 'Enstrophy density':
					scalar = vortices.enstrophyDensity()
				elif self.whichScalar_LocalData == 'Enstrophy Prod. Rate':
					scalar = vortices.enstrophyProductionRate()
				elif self.whichScalar_LocalData == 'Velocity x':
					scalar = velx
				elif self.whichScalar_LocalData == 'Velocity y':
					scalar = vely
				elif self.whichScalar_LocalData == 'Velocity z':
					scalar = velz
				elif self.whichScalar_LocalData == 'Vorticity x':
					scalar = vortx
				elif self.whichScalar_LocalData == 'Vorticity y':
					scalar = vorty
				elif self.whichScalar_LocalData == 'Vorticity z':
					scalar = vortz
				
				# Assign data to time series 1. TODO - Backup if TS already exists.
				
				self.u1[:, :, :, ctr] = velx
				self.v1[:, :, :, ctr] = vely
				self.w1[:, :, :, ctr] = velz
				self.omega1[:, :, :, ctr] = vortx
				self.omega2[:, :, :, ctr] = vorty
				self.omega3[:, :, :, ctr] = vortz
				self._dataTs1[:, :, :, ctr] = scalar
				
				ctr += 1
				fileCtr += skipTs
			
			# Update x, y, z data as well. Necessary if the visualization was
			# performed for different resolution
			
			self.x1 = np.float32(xx)
			self.y1 = np.float32(yy)
			self.z1 = np.float32(zz)
			
			self.dx_data1 = np.float32(dx)
			self.dy_data1 = np.float32(dy)
			self.dz_data1 = np.float32(dz)
			
			if self.altBBox:
				self.xlength_data1 = xmax_reconn - xmin_reconn
				self.ylength_data1 = ymax_reconn - ymin_reconn
				self.zlength_data1 = zmax_reconn - zmin_reconn
			else:
				self.xlength_data1 = int(self.xres_Local)
				self.ylength_data1 = int(self.yres_Local)
				self.zlength_data1 = int(self.zres_Local)
			
			self.xmin_data1 = float(self.xmin_Local)
			self.xmax_data1 = float(self.xmax_Local)
			self.ymin_data1 = float(self.ymin_Local)
			self.ymax_data1 = float(self.ymax_Local)
			self.zmin_data1 = float(self.zmin_Local)
			self.zmax_data1 = float(self.zmax_Local)
				
			# Choose the last time step to force refresh
			# Doesn't work when only one time step is calculated
			
			self.whichTime1 = (maxTs-minTs)//skipTs - 1
			
			# Adjust slice lengths and reconnection trim lengths

			self.slice_maxx1 = self.xlength_data1
			self.slice_maxy1 = self.ylength_data1
			self.slice_maxz1 = self.zlength_data1
			
			self.maxx1 = self.xlength_data1
			self.maxy1 = self.ylength_data1
			self.maxz1 = self.zlength_data1
			
			# Remove existing outlines as well
			self.out1_sc1.remove()
			self.sf1_sc1.remove()
			self.iso1_sc1.remove()
			
