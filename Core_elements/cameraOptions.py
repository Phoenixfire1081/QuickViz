# Supplement to Mayavi Visualization
# All camera options are defined here

from traits.api import on_trait_change
import numpy as np
from mayavi import mlab
import os

class allCameraOptions:

	@on_trait_change('updateCurrentVals')
	def updateCurrentVals_button_fired(self):
		
		# Get current cam values and update for screen 1
		if self.cam_screens == '1':
			self.camAzimuthG, self.camElevationG, self.camDistanceG, fp = mlab.view(figure=self.scene1.mayavi_scene)	
			self.focalPointG1, self.focalPointG2, self.focalPointG3 = fp
			self.camRollG = mlab.roll(figure=self.scene1.mayavi_scene)
		
		# Get current cam values and update for screen 2
		if self.cam_screens == '2':
			self.camAzimuthG, self.camElevationG, self.camDistanceG, fp = mlab.view(figure=self.scene2.mayavi_scene)	
			self.focalPointG1, self.focalPointG2, self.focalPointG3 = fp
			self.camRollG = mlab.roll(figure=self.scene2.mayavi_scene)
		
		# Get current cam values and update for screen 3
		if self.cam_screens == '3':
			self.camAzimuthG, self.camElevationG, self.camDistanceG, fp = mlab.view(figure=self.scene3.mayavi_scene)	
			self.focalPointG1, self.focalPointG2, self.focalPointG3 = fp
			self.camRollG = mlab.roll(figure=self.scene3.mayavi_scene)
		
		# Get current cam values and update for screen 4
		if self.cam_screens == '4':
			self.camAzimuthG, self.camElevationG, self.camDistanceG, fp = mlab.view(figure=self.scene4.mayavi_scene)	
			self.focalPointG1, self.focalPointG2, self.focalPointG3 = fp
			self.camRollG = mlab.roll(figure=self.scene4.mayavi_scene)
		
		# Round off values to make the GUI neat
		self.camAzimuthG = np.round(self.camAzimuthG, 2)
		self.camElevationG = np.round(self.camElevationG, 2)
		self.camDistanceG = np.round(self.camDistanceG, 2)
		self.focalPointG1 = np.round(self.focalPointG1, 2)
		self.focalPointG2 = np.round(self.focalPointG2, 2)
		self.focalPointG3 = np.round(self.focalPointG3, 2)
		self.camRollG = np.round(self.camRollG, 2)
		
		# Update setting options too
		self.camAzimuthS = np.round(self.camAzimuthG, 2)
		self.camElevationS = np.round(self.camElevationG, 2)
		self.camDistanceS = np.round(self.camDistanceG, 2)
		self.focalPointS1 = np.round(self.focalPointG1, 2)
		self.focalPointS2 = np.round(self.focalPointG2, 2)
		self.focalPointS3 = np.round(self.focalPointG3, 2)
		self.camRollS = np.round(self.camRollG, 2)
	
	def getValsForScene(self, whichScene):
		
		camAzimuth, camElevation, camDistance, fp = mlab.view(figure=whichScene)	
		fp1, fp2, fp3 = fp
		camRoll = mlab.roll(figure=whichScene)
		
		return camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll
	
	def saveState(self, filename):
		
		# Save state for all screens
		
		fw = open(filename, 'w+')
		
		camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = self.getValsForScene(self.scene1.mayavi_scene)
		
		fw.write(str(np.float32(camAzimuth)) + ' ' + \
				str(np.float32(camElevation)) + ' ' + \
				str(np.float32(camDistance)) + ' ' + \
				str(np.float32(fp1)) + ' ' + \
				str(np.float32(fp2)) + ' ' + \
				str(np.float32(fp3)) + ' ' + \
				str(np.float32(camRoll)) + '\n' 
				)
		
		camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = self.getValsForScene(self.scene2.mayavi_scene)
		
		fw.write(str(np.float32(camAzimuth)) + ' ' + \
				str(np.float32(camElevation)) + ' ' + \
				str(np.float32(camDistance)) + ' ' + \
				str(np.float32(fp1)) + ' ' + \
				str(np.float32(fp2)) + ' ' + \
				str(np.float32(fp3)) + ' ' + \
				str(np.float32(camRoll)) + '\n' 
				)
		
		camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = self.getValsForScene(self.scene3.mayavi_scene)
		
		fw.write(str(np.float32(camAzimuth)) + ' ' + \
				str(np.float32(camElevation)) + ' ' + \
				str(np.float32(camDistance)) + ' ' + \
				str(np.float32(fp1)) + ' ' + \
				str(np.float32(fp2)) + ' ' + \
				str(np.float32(fp3)) + ' ' + \
				str(np.float32(camRoll)) + '\n' 
				)
		
		camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = self.getValsForScene(self.scene4.mayavi_scene)
		
		fw.write(str(np.float32(camAzimuth)) + ' ' + \
				str(np.float32(camElevation)) + ' ' + \
				str(np.float32(camDistance)) + ' ' + \
				str(np.float32(fp1)) + ' ' + \
				str(np.float32(fp2)) + ' ' + \
				str(np.float32(fp3)) + ' ' + \
				str(np.float32(camRoll)) + '\n' 
				)
		
		fw.close()
	
	def loadState(self, filename):
		
		camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt(filename, max_rows = 1)
				
		mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene1.mayavi_scene)
		mlab.roll(camRoll, figure=self.scene1.mayavi_scene)
		
		camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt(filename, skiprows = 1, max_rows = 1)
			
		mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene2.mayavi_scene)
		mlab.roll(camRoll, figure=self.scene2.mayavi_scene)
		
		camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt(filename, skiprows = 2, max_rows = 1)
			
		mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene3.mayavi_scene)
		mlab.roll(camRoll, figure=self.scene3.mayavi_scene)
		
		camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt(filename, skiprows = 3, max_rows = 1)
			
		mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene4.mayavi_scene)
		mlab.roll(camRoll, figure=self.scene4.mayavi_scene)
	
	def loadStateHelper(self, filename):
		
		if os.path.isfile(filename):
			
			# Load up all scenes
			
			self.loadState(filename)
		
		else:
			
			self.saveState(filename)
	
	@on_trait_change('saveCam1')
	def saveCam1_fired(self):
		
		# Save and load camera state
		
		self.loadStateHelper('cam1.txt')
		
		# Update camera values
		self.updateCurrentVals_button_fired()
	
	@on_trait_change('saveCam2')
	def saveCam2_fired(self):
		
		# Save and load camera state
		
		self.loadStateHelper('cam2.txt')
		
		# Update camera values
		self.updateCurrentVals_button_fired()
	
	@on_trait_change('saveCam3')
	def saveCam3_fired(self):
		
		# Save and load camera state
		
		self.loadStateHelper('cam3.txt')
		
		# Update camera values
		self.updateCurrentVals_button_fired()
	
	@on_trait_change('saveCam4')
	def saveCam4_fired(self):
		
		# Save and load camera state
		
		self.loadStateHelper('cam4.txt')
		
		# Update camera values
		self.updateCurrentVals_button_fired()
	
	@on_trait_change('saveCam5')
	def saveCam5_fired(self):
		
		# Save and load camera state
		
		self.loadStateHelper('cam4.txt')
		
		# Update camera values
		self.updateCurrentVals_button_fired()
		
	@on_trait_change('camReset')
	def camReset_fired(self):
		
		# Remove all camera orientation files
		os.system('rm -rf cam1.txt cam2.txt cam3.txt cam4.txt cam5.txt')
		
	@on_trait_change('camAzimuthS, camElevationS, camDistanceS, \
	focalPointS1, focalPointS2, focalPointS3, camRollS')
	def cam_angle_changed(self):
		
		# Update camera view for screen 1
		if self.cam_screens == '1':
			mlab.view(self.camAzimuthS, self.camElevationS, self.camDistanceS, [self.focalPointS1, self.focalPointS2, self.focalPointS3], figure=self.scene1.mayavi_scene)
			mlab.roll(self.camRollS, figure=self.scene1.mayavi_scene)
		
		# Update camera view for screen 2
		if self.cam_screens == '2':
			mlab.view(self.camAzimuthS, self.camElevationS, self.camDistanceS, [self.focalPointS1, self.focalPointS2, self.focalPointS3], figure=self.scene2.mayavi_scene)
			mlab.roll(self.camRollS, figure=self.scene2.mayavi_scene)
		
		# Update camera view for screen 3
		if self.cam_screens == '3':
			mlab.view(self.camAzimuthS, self.camElevationS, self.camDistanceS, [self.focalPointS1, self.focalPointS2, self.focalPointS3], figure=self.scene3.mayavi_scene)
			mlab.roll(self.camRollS, figure=self.scene3.mayavi_scene)
		
		# Update camera view for screen 4
		if self.cam_screens == '4':
			mlab.view(self.camAzimuthS, self.camElevationS, self.camDistanceS, [self.focalPointS1, self.focalPointS2, self.focalPointS3], figure=self.scene4.mayavi_scene)
			mlab.roll(self.camRollS, figure=self.scene4.mayavi_scene)
		
