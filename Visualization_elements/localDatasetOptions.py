# Supplement to QuickViz
# All local dataset options are defined here

from traits.api import on_trait_change
import numpy as np
from .vortexExtraction import vortexExtract
from ..Core_elements.tKinter import folderBrowser
# from ..Core_elements.timeUpdate import timeUpdateBehavior
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
	
	def save_data_actual(self):
		
		if not self.timeStep_LocalData == '':
		
			if '-' in self.timeStep_LocalData:
				minTs = int(self.timeStep_LocalData.split('-')[0])
				maxTs = int(self.timeStep_LocalData.split('-')[1])
				
				# Check if skip values are provided
				try: 
					skipTs = int(self.timeStep_LocalData.split('-')[2])
				except:
					skipTs = 1
				
			else:
				minTs = int(self.timeStep_LocalData)
				maxTs = int(self.timeStep_LocalData)
				skipTs = 1
			
			# Create appropriate folders first
			
			os.makedirs(self.save_path + '/' + self.folderNameExport, exist_ok=True)
			
			if self.saveWhatOptions == 'Computed scalar':
				# if not os.path.exists(self.save_path + '/' + self.folderNameExport):
				os.makedirs(self.save_path + '/' + self.folderNameExport + '/scalar', exist_ok=True)
				folderPath = self.save_path + '/' + self.folderNameExport + '/scalar/'
			
			elif self.saveWhatOptions == 'Velocity data':
				# if not os.path.exists(self.save_path + '/' + self.folderNameExport):
				os.makedirs(self.save_path + '/' + self.folderNameExport + '/velComp', exist_ok=True)
				folderPath = self.save_path + '/' + self.folderNameExport + '/velComp/'
			
			elif self.saveWhatOptions == 'Vorticity data':
				# if not os.path.exists(self.save_path + '/' + self.folderNameExport):
				os.makedirs(self.save_path + '/' + self.folderNameExport + '/vortComp', exist_ok=True)
				folderPath = self.save_path + '/' + self.folderNameExport + '/vortComp/'
			
			ctr = 1
			
			if self.altBBox:
				
				xmin_reconn = self.whichSliceX1_reconn
				xmax_reconn = self.whichSliceX2_reconn
				ymin_reconn = self.whichSliceY1_reconn
				ymax_reconn = self.whichSliceY2_reconn
				zmin_reconn = self.whichSliceZ1_reconn
				zmax_reconn = self.whichSliceZ2_reconn
			
			for ts in range(minTs, maxTs+1, skipTs):
			
				if self.assignToTS == 'Time Series 1': # Save data from TS1
					
					if self.saveWhatOptions == 'Computed scalar':
						scalar = self._dataTs1[:, :, :, ts]
					
					elif self.saveWhatOptions == 'Velocity data':
						u = self.u1[:, :, :, ts]
						v = self.v1[:, :, :, ts]
						w = self.w1[:, :, :, ts]
					
					elif self.saveWhatOptions == 'Velocity data':
						om1 = self.omega1[:, :, :, ts]
						om2 = self.omega2[:, :, :, ts]
						om3 = self.omega3[:, :, :, ts]
					
				if self.assignToTS == 'Time Series 2': # Save data from TS2
					
					if self.saveWhatOptions == 'Computed scalar':
						scalar = self._dataTs2[:, :, :, ts]
					
					elif self.saveWhatOptions == 'Velocity data':
						u = self.u2[:, :, :, ts]
						v = self.v2[:, :, :, ts]
						w = self.w2[:, :, :, ts]
					
					elif self.saveWhatOptions == 'Velocity data':
						om1 = self.omega1_2[:, :, :, ts]
						om2 = self.omega2_2[:, :, :, ts]
						om3 = self.omega3_2[:, :, :, ts]
					
				if self.assignToTS == 'Time Series 3': # Save data from TS3
					
					if self.saveWhatOptions == 'Computed scalar':
						scalar = self._dataTs3[:, :, :, ts]
					
					elif self.saveWhatOptions == 'Velocity data':
						u = self.u3[:, :, :, ts]
						v = self.v3[:, :, :, ts]
						w = self.w3[:, :, :, ts]
					
					elif self.saveWhatOptions == 'Velocity data':
						om1 = self.omega1_3[:, :, :, ts]
						om2 = self.omega2_3[:, :, :, ts]
						om3 = self.omega3_3[:, :, :, ts]
					
				if self.assignToTS == 'Time Series 4': # Save data from TS4
					
					if self.saveWhatOptions == 'Computed scalar':
						scalar = self._dataTs4[:, :, :, ts]
					
					elif self.saveWhatOptions == 'Velocity data':
						u = self.u4[:, :, :, ts]
						v = self.v4[:, :, :, ts]
						w = self.w4[:, :, :, ts]
					
					elif self.saveWhatOptions == 'Velocity data':
						om1 = self.omega1_4[:, :, :, ts]
						om2 = self.omega2_4[:, :, :, ts]
						om3 = self.omega3_4[:, :, :, ts]
				
				if self.altBBox:
					
					if self.saveWhatOptions == 'Computed scalar':
						scalar = scalar[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]
					
					elif self.saveWhatOptions == 'Velocity data':
						u = u[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]
						v = v[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]
						w = w[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]
					
					elif self.saveWhatOptions == 'Velocity data':
						om1 = om1[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]
						om2 = om2[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]
						om3 = om3[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]
					
				if self.saveWhatOptions == 'Computed scalar':
					
					fw = open(folderPath + 'scalar_' + str(ctr).zfill(4) + '.bin', 'wb')
					scalar.tofile(fw)
					fw.close()
				
				elif self.saveWhatOptions == 'Velocity data':
					
					fw = open(folderPath + 'velx_' + str(ctr).zfill(4) + '.bin', 'wb')
					u.tofile(fw)
					fw.close()
					
					fw = open(folderPath + 'vely_' + str(ctr).zfill(4) + '.bin', 'wb')
					v.tofile(fw)
					fw.close()
					
					fw = open(folderPath + 'velz_' + str(ctr).zfill(4) + '.bin', 'wb')
					w.tofile(fw)
					fw.close()
				
				elif self.saveWhatOptions == 'Vorticity data':
					
					fw = open(folderPath + 'velx_' + str(ctr).zfill(4) + '.bin', 'wb')
					om1.tofile(fw)
					fw.close()
					
					fw = open(folderPath + 'vely_' + str(ctr).zfill(4) + '.bin', 'wb')
					om2.tofile(fw)
					fw.close()
					
					fw = open(folderPath + 'velz_' + str(ctr).zfill(4) + '.bin', 'wb')
					om3.tofile(fw)
					fw.close()
				
				ctr += 1
	
	def reset_specific_ts(self, xres, yres, zres, numFiles, whichTs):
		
		if whichTs == 1:
			if not self.scalarOnly:	
				self.u1 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.v1 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.w1 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.omega1 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.omega2 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.omega3 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
			else:	
				self.u1 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.v1 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.w1 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.omega1 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.omega2 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.omega3 = np.zeros((3, 3, 3, 1), dtype = np.float32)
			self._dataTs1 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
		
		if whichTs == 2:
			if not self.scalarOnly:	
				self.u2 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.v2 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.w2 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.omega1_2 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.omega2_2 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.omega3_2 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
			else:
				self.u2 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.v2 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.w2 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.omega1_2 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.omega2_2 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.omega3_2 = np.zeros((3, 3, 3, 1), dtype = np.float32)
			self._dataTs2 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
		
		if whichTs == 3:
			if not self.scalarOnly:	
				self.u3 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.v3 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.w3 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.omega1_3 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.omega2_3 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.omega3_3 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
			else:
				self.u3 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.v3 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.w3 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.omega1_3 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.omega2_3 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.omega3_3 = np.zeros((3, 3, 3, 1), dtype = np.float32)
			self._dataTs3 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
		
		if whichTs == 4:
			if not self.scalarOnly:	
				self.u4 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.v4 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.w4 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.omega1_4 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.omega2_4 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
				self.omega3_4 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
			else:
				self.u4 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.v4 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.w4 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.omega1_4 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.omega2_4 = np.zeros((3, 3, 3, 1), dtype = np.float32)
				self.omega3_4 = np.zeros((3, 3, 3, 1), dtype = np.float32)
			self._dataTs4 = np.zeros((xres, yres, zres, numFiles), dtype = np.float32)
			
	def write_to_specific_ts(self, velx, vely, velz, vortx, vorty, vortz, scalar, xx, yy, zz, dx, dy, dz, xres, yres, zres, ctr, maxTs, minTs, skipTs):
		
		# TODO - calculate on demand, vorticity data can be calculated on demand to save RAM space. Loading velocity data can be made optional
		
		if self.assignToTS == 'Time Series 1':
			
			if not self.scalarOnly:	
				self.u1[:, :, :, ctr] = velx
				self.v1[:, :, :, ctr] = vely
				self.w1[:, :, :, ctr] = velz
				self.omega1[:, :, :, ctr] = vortx
				self.omega2[:, :, :, ctr] = vorty
				self.omega3[:, :, :, ctr] = vortz
			self._dataTs1[:, :, :, ctr] = scalar
			
			# Update x, y, z data as well. Necessary if the visualization was
			# performed for different resolution

			self.x1 = np.float32(xx)
			self.y1 = np.float32(yy)
			self.z1 = np.float32(zz)

			self.dx_data1 = np.float32(dx)
			self.dy_data1 = np.float32(dy)
			self.dz_data1 = np.float32(dz)
			
			self.xlength_data1 = int(xres)
			self.ylength_data1 = int(yres)
			self.zlength_data1 = int(zres)

			self.xmin_data1 = float(self.xmin_Local)
			self.xmax_data1 = float(self.xmax_Local)
			self.ymin_data1 = float(self.ymin_Local)
			self.ymax_data1 = float(self.ymax_Local)
			self.zmin_data1 = float(self.zmin_Local)
			self.zmax_data1 = float(self.zmax_Local)
				
			# Adjust slice lengths and reconnection trim lengths

			self.slice_maxx1 = self.xlength_data1
			self.slice_maxy1 = self.ylength_data1
			self.slice_maxz1 = self.zlength_data1

			self.maxx1 = self.xlength_data1
			self.maxy1 = self.ylength_data1
			self.maxz1 = self.zlength_data1
			
			self.numTs1 = ctr
			self.whichTime1 = 1
			self.whichTime1 = 0
			
			self.ts1max = (maxTs - minTs)//skipTs - 1 # This updates the slider
		
		elif self.assignToTS == 'Time Series 2':
			
			if not self.scalarOnly:	
				self.u2[:, :, :, ctr] = velx
				self.v2[:, :, :, ctr] = vely
				self.w2[:, :, :, ctr] = velz
				self.omega1_2[:, :, :, ctr] = vortx
				self.omega2_2[:, :, :, ctr] = vorty
				self.omega3_2[:, :, :, ctr] = vortz
			self._dataTs2[:, :, :, ctr] = scalar
			
			# Update x, y, z data as well. Necessary if the visualization was
			# performed for different resolution

			self.x2 = np.float32(xx)
			self.y2 = np.float32(yy)
			self.z2 = np.float32(zz)

			self.dx_data2 = np.float32(dx)
			self.dy_data2 = np.float32(dy)
			self.dz_data2 = np.float32(dz)
			
			self.xlength_data2 = int(xres)
			self.ylength_data2 = int(yres)
			self.zlength_data2 = int(zres)

			self.xmin_data2 = float(self.xmin_Local)
			self.xmax_data2 = float(self.xmax_Local)
			self.ymin_data2 = float(self.ymin_Local)
			self.ymax_data2 = float(self.ymax_Local)
			self.zmin_data2 = float(self.zmin_Local)
			self.zmax_data2 = float(self.zmax_Local)
				
			# Adjust slice lengths and reconnection trim lengths

			self.slice_maxx2 = self.xlength_data2
			self.slice_maxy2 = self.ylength_data2
			self.slice_maxz2 = self.zlength_data2

			self.maxx2 = self.xlength_data2
			self.maxy2 = self.ylength_data2
			self.maxz2 = self.zlength_data2
			
			self.nts = 2
			self.numTs2 = ctr
			
			self.whichTime2 = 1
			self.whichTime2 = 0
			
			self.ts2max = (maxTs - minTs)//skipTs - 1 # This updates the slider
			
		elif self.assignToTS == 'Time Series 3':
			
			if not self.scalarOnly:	
				self.u3[:, :, :, ctr] = velx
				self.v3[:, :, :, ctr] = vely
				self.w3[:, :, :, ctr] = velz
				self.omega1_3[:, :, :, ctr] = vortx
				self.omega2_3[:, :, :, ctr] = vorty
				self.omega3_3[:, :, :, ctr] = vortz
			self._dataTs3[:, :, :, ctr] = scalar
			
			# Update x, y, z data as well. Necessary if the visualization was
			# performed for different resolution

			self.x3 = np.float32(xx)
			self.y3 = np.float32(yy)
			self.z3 = np.float32(zz)

			self.dx_data3 = np.float32(dx)
			self.dy_data3 = np.float32(dy)
			self.dz_data3 = np.float32(dz)
			
			self.xlength_data3 = int(xres)
			self.ylength_data3 = int(yres)
			self.zlength_data3 = int(zres)

			self.xmin_data3 = float(self.xmin_Local)
			self.xmax_data3 = float(self.xmax_Local)
			self.ymin_data3 = float(self.ymin_Local)
			self.ymax_data3 = float(self.ymax_Local)
			self.zmin_data3 = float(self.zmin_Local)
			self.zmax_data3 = float(self.zmax_Local)
				
			# Adjust slice lengths and reconnection trim lengths

			self.slice_maxx3 = self.xlength_data3
			self.slice_maxy3 = self.ylength_data3
			self.slice_maxz3 = self.zlength_data3

			self.maxx3 = self.xlength_data3
			self.maxy3 = self.ylength_data3
			self.maxz3 = self.zlength_data3
			
			self.nts = 3
			self.numTs3 = ctr
			
			self.whichTime3 = 1
			self.whichTime3 = 0
			
			self.ts3max = (maxTs - minTs)//skipTs - 1 # This updates the slider
			
		elif self.assignToTS == 'Time Series 4':
			
			if not self.scalarOnly:	
				self.u4[:, :, :, ctr] = velx
				self.v4[:, :, :, ctr] = vely
				self.w4[:, :, :, ctr] = velz
				self.omega1_4[:, :, :, ctr] = vortx
				self.omega2_4[:, :, :, ctr] = vorty
				self.omega3_4[:, :, :, ctr] = vortz
			self._dataTs4[:, :, :, ctr] = scalar
			
			# Update x, y, z data as well. Necessary if the visualization was
			# performed for different resolution

			self.x4 = np.float32(xx)
			self.y4 = np.float32(yy)
			self.z4 = np.float32(zz)

			self.dx_data4 = np.float32(dx)
			self.dy_data4 = np.float32(dy)
			self.dz_data4 = np.float32(dz)
			
			self.xlength_data4 = int(xres)
			self.ylength_data4 = int(yres)
			self.zlength_data4 = int(zres)

			self.xmin_data4 = float(self.xmin_Local)
			self.xmax_data4 = float(self.xmax_Local)
			self.ymin_data4 = float(self.ymin_Local)
			self.ymax_data4 = float(self.ymax_Local)
			self.zmin_data4 = float(self.zmin_Local)
			self.zmax_data4 = float(self.zmax_Local)
				
			# Adjust slice lengths and reconnection trim lengths

			self.slice_maxx4 = self.xlength_data4
			self.slice_maxy4 = self.ylength_data4
			self.slice_maxz4 = self.zlength_data4

			self.maxx4 = self.xlength_data4
			self.maxy4 = self.ylength_data4
			self.maxz4 = self.zlength_data4
			
			self.nts = 4
			self.numTs4 = ctr
			
			self.whichTime4 = 1
			self.whichTime4 = 0
			
			self.ts4max = (maxTs - minTs)//skipTs - 1 # This updates the slider
			
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
			
				# Get time step data (calculate from velocity folder or scalar folder)
				try:
					self.timeSteps_LocalData = str(len(os.listdir(self.LocalData_path + '/velComp/'))//3)
				except FileNotFoundError:
					self.timeSteps_LocalData = str(len(os.listdir(self.LocalData_path + '/scalar/')))
			
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
		self.maxx1 = int(self.xres_Local)
		self.maxy1 = int(self.yres_Local)
		self.maxz1 = int(self.zres_Local)
			
	@on_trait_change('load_LocalData')
	def load_LocalData_fired(self):
		
		# TODO - this can be combined with real space visualization
		# TODO - import with specific timesteps, similar to real space visualization, done
		# TODO - store specific scalar data?
		
		if self.assignToTS == 'Time Series 1':
			whichTs = 1
		if self.assignToTS == 'Time Series 2':
			whichTs = 2
		if self.assignToTS == 'Time Series 3':
			whichTs = 3
		if self.assignToTS == 'Time Series 4':
			whichTs = 4
		
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
				maxTs = int(self.timeStep_LocalData.split('-')[1])
				
				# Check if skip values are provided
				try: 
					skipTs = int(self.timeStep_LocalData.split('-')[2])
				except:
					skipTs = 1
				
			else:
				minTs = int(self.timeStep_LocalData)
				maxTs = int(self.timeStep_LocalData)
				skipTs = 1
			
			# Completely replace TS with new data
			
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
				
				numFiles = int(np.ceil((maxTs - minTs)/skipTs))
				self.reset_specific_ts(xres_alt, yres_alt, zres_alt, numFiles, whichTs)
				
			else:
				
				numFiles = int(np.ceil((maxTs - minTs)/skipTs))
				self.reset_specific_ts(int(self.xres_Local), int(self.yres_Local), int(self.zres_Local), numFiles, whichTs)
			
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
				
				if self.whichScalar_LocalData == 'Available scalar':
					flist_sc = os.listdir(self.LocalData_path + '/scalar/')
					flist_sc = [i for i in flist_sc if not i.startswith('.')] # ignores hidden files
					flist_sc.sort(key = lambda x:int(x.split('_')[1].split('.')[0]))
				
				else:
			
					# Get file list
					flist = os.listdir(self.LocalData_path + '/velComp/')
					flist_x = [i for i in flist if 'velx' in i]
					flist_y = [i for i in flist if 'vely' in i]
					flist_z = [i for i in flist if 'velz' in i]
					flist_x.sort(key = lambda x:int(x.split('_')[1].split('.')[0]))
					flist_y.sort(key = lambda x:int(x.split('_')[1].split('.')[0]))
					flist_z.sort(key = lambda x:int(x.split('_')[1].split('.')[0]))
				
				
			
			print(minTs, maxTs, skipTs)
			for ts in range(minTs, maxTs, skipTs):
				
				if self.allLocalDatasetOptions == 'Raw 3D':
					
					# Use array.array to dump velocity data into memory
					# For now, force data as single precision. TODO - support double precision data
					
					if not self.whichScalar_LocalData == 'Available scalar':
					
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
					
				# Compute vorticity vector if not scalar only and requested scalar
				if not self.whichScalar_LocalData == 'Available scalar':
					vortices = vortexExtract(velx, vely, velz, dx, dy, dz)
					vortx, vorty, vortz = vortices.vorticityComponents()
				else:
					velx = np.zeros((3, 3, 3, 1), dtype = float)
					vely = np.zeros((3, 3, 3, 1), dtype = float)
					velz = np.zeros((3, 3, 3, 1), dtype = float)
					vortx = np.zeros((3, 3, 3, 1), dtype = float)
					vorty = np.zeros((3, 3, 3, 1), dtype = float)
					vortz = np.zeros((3, 3, 3, 1), dtype = float)
				
				if self.whichScalar_LocalData == 'Available scalar' and self.allLocalDatasetOptions == 'Raw 3D':
					tmp = array.array(_dtype)
					tmp.fromfile(open(self.LocalData_path + '/scalar/' + flist_sc[fileCtr], 'rb'), (DataRes))
					tmp = np.reshape(tmp, [int(self.xres_Local), int(self.yres_Local), int(self.zres_Local)])
					if self.altBBox:
						tmp = tmp[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn]
					scalar = tmp
				elif self.whichScalar_LocalData == 'Available scalar' and self.allLocalDatasetOptions == 'netCDF':
					tmp = np.asarray(np.float32(data[self.scalarLabel][:]))
					if self.altBBox:
						tmp = tmp[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn]
					scalar = tmp
				elif self.whichScalar_LocalData == 'Velocity magnitude':
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
				
				# Assign data to the requested time series
				
				if self.altBBox:
					self.write_to_specific_ts(velx, vely, velz, vortx, vorty, vortz, scalar, xx, yy, zz, dx, dy, dz, xmax_reconn - xmin_reconn, ymax_reconn - ymin_reconn, zmax_reconn - zmin_reconn, ctr, maxTs, minTs, skipTs)
				else:
					self.write_to_specific_ts(velx, vely, velz, vortx, vorty, vortz, scalar, xx, yy, zz, dx, dy, dz, int(self.xres_Local), int(self.yres_Local), int(self.zres_Local), ctr, maxTs, minTs, skipTs)
				
				# Choose the last time step to force refresh
				# Doesn't work when only one time step is calculated

				# self.whichTime1 = int(np.ceil((maxTs-minTs)/skipTs) - 2)
				# forceupdate = timeUpdateBehavior()
				# forceupdate.force_update()
				
				ctr += 1
				fileCtr += skipTs
			
			# try:
			
				# # Remove existing outlines as well
				# self.out1_sc1.remove()
				# self.sf1_sc1.remove()
				# self.iso1_sc1.remove()
			
			# except ValueError: # Fixes issue when trying to load the data multiple times
				
				# pass
			
			# After loading is completed, restore original data to TS1. NOTE: Data is reset while choosing the folder
			
			if not self.assignToTS == 'Time Series 1':
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
			
	@on_trait_change('exportNow')
	def exportNow_fired(self):
		
		print('Save path:', self.save_path)
		print('Folder:', self.folderNameExport)
		print(self.save_path + '/' + self.folderNameExport)
		
		self.save_data_actual()
		
		# Write how to read file
		
		if self.altBBox:
			xres = self.whichSliceX2_reconn - self.whichSliceX1_reconn
			yres = self.whichSliceY2_reconn - self.whichSliceY1_reconn
			zres = self.whichSliceZ2_reconn - self.whichSliceZ1_reconn
			
			xmin_reconn = self.whichSliceX1_reconn
			xmax_reconn = self.whichSliceX2_reconn
			ymin_reconn = self.whichSliceY1_reconn
			ymax_reconn = self.whichSliceY2_reconn
			zmin_reconn = self.whichSliceZ1_reconn
			zmax_reconn = self.whichSliceZ2_reconn
		
		if self.assignToTS ==  'Time Series 1':
			if self.altBBox:
				xmin = np.min(np.unique(self.x1[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				xmax = np.max(np.unique(self.x1[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				ymin = np.min(np.unique(self.y1[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				ymax = np.max(np.unique(self.y1[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				zmin = np.min(np.unique(self.z1[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				zmax = np.max(np.unique(self.z1[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
			else:
				xmin = np.min(np.unique(self.x1))
				xmax = np.max(np.unique(self.x1))
				ymin = np.min(np.unique(self.y1))
				ymax = np.max(np.unique(self.y1))
				zmin = np.min(np.unique(self.z1))
				zmax = np.max(np.unique(self.z1))
				xres, yres, zres = np.shape(self.x1)
		elif self.assignToTS ==  'Time Series 2':
			if self.altBBox:
				xmin = np.min(np.unique(self.x2[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				xmax = np.max(np.unique(self.x2[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				ymin = np.min(np.unique(self.y2[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				ymax = np.max(np.unique(self.y2[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				zmin = np.min(np.unique(self.z2[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				zmax = np.max(np.unique(self.z2[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
			else:
				xmin = np.min(np.unique(self.x2))
				xmax = np.max(np.unique(self.x2))
				ymin = np.min(np.unique(self.y2))
				ymax = np.max(np.unique(self.y2))
				zmin = np.min(np.unique(self.z2))
				zmax = np.max(np.unique(self.z2))
				xres, yres, zres = np.shape(self.x2)
		elif self.assignToTS ==  'Time Series 3':
			if self.altBBox:
				xmin = np.min(np.unique(self.x3[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				xmax = np.max(np.unique(self.x3[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				ymin = np.min(np.unique(self.y3[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				ymax = np.max(np.unique(self.y3[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				zmin = np.min(np.unique(self.z3[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				zmax = np.max(np.unique(self.z3[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
			else:
				xmin = np.min(np.unique(self.x3))
				xmax = np.max(np.unique(self.x3))
				ymin = np.min(np.unique(self.y3))
				ymax = np.max(np.unique(self.y3))
				zmin = np.min(np.unique(self.z3))
				zmax = np.max(np.unique(self.z3))
				xres, yres, zres = np.shape(self.x3)
		elif self.assignToTS ==  'Time Series 4':
			if self.altBBox:
				xmin = np.min(np.unique(self.x4[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				xmax = np.max(np.unique(self.x4[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				ymin = np.min(np.unique(self.y4[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				ymax = np.max(np.unique(self.y4[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				zmin = np.min(np.unique(self.z4[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
				zmax = np.max(np.unique(self.z4[xmin_reconn: xmax_reconn, ymin_reconn: ymax_reconn, zmin_reconn: zmax_reconn]))
			else:
				xmin = np.min(np.unique(self.x4))
				xmax = np.max(np.unique(self.x4))
				ymin = np.min(np.unique(self.y4))
				ymax = np.max(np.unique(self.y4))
				zmin = np.min(np.unique(self.z4))
				zmax = np.max(np.unique(self.z4))
				xres, yres, zres = np.shape(self.x4)
		
		fw = open(self.save_path + '/' + self.folderNameExport + '/howToRead.txt', 'w+')
		fw.write('Bounding Box:\n\
xmin xmax ymin ymax zmin zmax\n')
		fw.write(str(xmin) + ' ' + str(xmax) + ' ' + str(ymin) + ' ' + str(ymax) + ' ' + str(zmin) + ' ' + str(zmax) + '\n')
		fw.write('Resolution:\n\
xres yres zres\n')
		fw.write(str(xres) + ' ' + str(yres) + ' ' + str(zres))
		fw.close()
