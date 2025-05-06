# Supplement to Mayavi Visualization
# All camera path controls are defined here

from traits.api import on_trait_change
import os
from mayavi import mlab
import numpy as np

class allPathControlsClass:
	
	def write_to_file(self):
		
		# Create camera path for every time step
			
		fw = open('cameraPath.txt', 'w+')
		
		# Get current camera values
		
		camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene1.mayavi_scene)	
		fp1, fp2, fp3 = fp
		camRoll = mlab.roll(figure=self.scene1.mayavi_scene)
		
		# File format
		# ts Azimuth Elevation Distance fp1 fp2 fp3 Roll Type(default is none)
		# type - 0 (None), 1 (Linear), 2 (Circle), 3 (Waypoints)
		for i in range(self.numTs1+1):
			fw.write(str(i) + ' ' + \
			str(np.float32(camAzimuth)) + ' ' + \
			str(np.float32(camElevation)) + ' ' + \
			str(np.float32(camDistance)) + ' ' + \
			str(np.float32(fp1)) + ' ' + \
			str(np.float32(fp2)) + ' ' + \
			str(np.float32(fp3)) + ' ' + \
			str(np.float32(camRoll)) + ' 0 \n')
		fw.close()
		
		# Read the data
		
		self.camPathData = np.loadtxt('cameraPath.txt')
	
	@on_trait_change('camPathType')
	def camPathTypeChanged(self):
		
		# Check if camera path file exists
		# NOTE: camera path works only for one screen
		# Assumes it's the first screen
		
		if os.path.isfile('cameraPath.txt'):
			
			self.camPathData = np.loadtxt('cameraPath.txt')
		
		else:
			
			self.write_to_file()
	
	@on_trait_change('addCamPath')
	def addCamPathChanged(self):
		
		# if -1, set to max ts
		if self.stopCamPath == -1:
			self.stopCamPath = self.numTs1
		
		totalSteps = (self.stopCamPath) - self.startCamPath
		
		# Get current camera values
		
		camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene1.mayavi_scene)	
		fp1, fp2, fp3 = fp
		camRoll = mlab.roll(figure=self.scene1.mayavi_scene)
		
		if self.camPathType == 'Circle':
			
			# Rotate Elevation only
			for i in range(int(self.startCamPath), int(self.stopCamPath+1)):
				elevationCalc = 180 * i / totalSteps
				
				# Update cam path data
				self.camPathData[i, 2] = elevationCalc
				self.camPathData[i, -1] = 1 # Corresponding to circle
		
		if self.camPathType == 'Linear':
			
			if np.sum(self.camPathData[:, -1]) == 0:
				self.camPathData *= 0
			
			# Store camera positions
			self.camPathData[self.whichTime1, 1] = camAzimuth
			self.camPathData[self.whichTime1, 2] = camElevation
			self.camPathData[self.whichTime1, 3] = camDistance
			self.camPathData[self.whichTime1, 4] = fp1
			self.camPathData[self.whichTime1, 5] = fp2
			self.camPathData[self.whichTime1, 6] = fp3
			self.camPathData[self.whichTime1, 7] = camRoll
			self.camPathData[self.whichTime1, 8] = 2 # Corresponding to Linear
	
	@on_trait_change('finishCamPath')
	def finishCamPathChanged(self):
		
		if self.camPathType == 'Circle':
			
			np.savetxt('cameraPath.txt', self.camPathData, delimiter = ' ', newline = '\n')
		
		if self.camPathType == 'Linear':
			
			totalSteps = (self.stopCamPath) - self.startCamPath
			step = 1/totalSteps
			
			# Get data first
			_, camAzimuth1, camElevation1, camDistance1, fp1_1, fp2_1, fp3_1, camRoll1, _ = self.camPathData[int(self.startCamPath)]
			_, camAzimuth2, camElevation2, camDistance2, fp1_2, fp2_2, fp3_2, camRoll2, _ = self.camPathData[int(self.stopCamPath)]
			
			# Interpolate linearly
			for i in range(int(self.startCamPath + 1), int(self.stopCamPath)):
				self.camPathData[i, 1] = (1 - step) * camAzimuth1 + step * camAzimuth2
				self.camPathData[i, 2] = (1 - step) * camElevation1 + step * camElevation2
				self.camPathData[i, 3] = (1 - step) * camDistance1 + step * camDistance2
				self.camPathData[i, 4] = (1 - step) * fp1_1 + step * fp1_2
				self.camPathData[i, 5] = (1 - step) * fp2_1 + step * fp2_2
				self.camPathData[i, 6] = (1 - step) * fp3_1 + step * fp3_2
				self.camPathData[i, 7] = (1 - step) * camRoll1 + step * camRoll2
				self.camPathData[i, 8] = 2 # Corresponding to linear
				step += (1/totalSteps)
			
			# Write to file	
			np.savetxt('cameraPath.txt', self.camPathData, delimiter = ' ', newline = '\n')
				
	@on_trait_change('resetCamPath')
	def resetCamPathChanged(self):
		
		self.write_to_file()
