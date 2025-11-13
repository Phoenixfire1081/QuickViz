# Supplement to Mayavi Visualization
# All camera options are defined here

from traits.api import on_trait_change
import numpy as np
from mayavi import mlab
import os

class allCameraOptions:

	@on_trait_change('updateCurrentVals')
	def updateCurrentVals_button_fired(self):
		
		# NOTE: If multiple screens are selected, the last one is shown
		# Get current cam values and update for screen 1
		if self.screen1_ts1:
			self.camAzimuthG, self.camElevationG, self.camDistanceG, fp = mlab.view(figure=self.scene1.mayavi_scene)	
			self.focalPointG1, self.focalPointG2, self.focalPointG3 = fp
			self.camRollG = mlab.roll(figure=self.scene1.mayavi_scene)
		
		# Get current cam values and update for screen 2
		if self.screen2_ts1:
			self.camAzimuthG, self.camElevationG, self.camDistanceG, fp = mlab.view(figure=self.scene2.mayavi_scene)	
			self.focalPointG1, self.focalPointG2, self.focalPointG3 = fp
			self.camRollG = mlab.roll(figure=self.scene2.mayavi_scene)
		
		# Get current cam values and update for screen 3
		if self.screen3_ts1:
			self.camAzimuthG, self.camElevationG, self.camDistanceG, fp = mlab.view(figure=self.scene3.mayavi_scene)	
			self.focalPointG1, self.focalPointG2, self.focalPointG3 = fp
			self.camRollG = mlab.roll(figure=self.scene3.mayavi_scene)
		
		# Get current cam values and update for screen 4
		if self.screen4_ts1:
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
	
	@on_trait_change('saveCam1')
	def saveCam1_fired(self):
		
		# Save and load camera state
		
		if os.path.isfile('cam1.txt'):
			
			if self.screen1_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam1.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene1.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene1.mayavi_scene)
			
			if self.screen2_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam1.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene2.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene2.mayavi_scene)
			
			if self.screen3_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam1.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene3.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene3.mayavi_scene)
			
			if self.screen4_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam1.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene4.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene4.mayavi_scene)
		
		else:
		
			# Get current cam values for active screen
			# NOTE: Only one screen can be active at a time
			if self.screen1_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene1.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene1.mayavi_scene)
				
				fw = open('cam1.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
			if self.screen2_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene2.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene2.mayavi_scene)
				
				fw = open('cam1.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
			if self.screen3_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene3.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene3.mayavi_scene)
				
				fw = open('cam1.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
			if self.screen4_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene4.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene4.mayavi_scene)
				
				fw = open('cam1.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
		
		# Update camera values
		self.updateCurrentVals_button_fired()
	
	@on_trait_change('saveCam2')
	def saveCam2_fired(self):
		
		# Save and load camera state
		
		if os.path.isfile('cam2.txt'):
			
			if self.screen1_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam2.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene1.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene1.mayavi_scene)
			
			if self.screen2_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam2.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene2.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene2.mayavi_scene)
			
			if self.screen3_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam2.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene3.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene3.mayavi_scene)
			
			if self.screen4_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam2.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene4.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene4.mayavi_scene)
		
		else:
		
			# Get current cam values for active screen
			# NOTE: Only one screen can be active at a time
			if self.screen1_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene1.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene1.mayavi_scene)
				
				fw = open('cam2.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
			if self.screen2_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene2.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene2.mayavi_scene)
				
				fw = open('cam2.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
			if self.screen3_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene3.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene3.mayavi_scene)
				
				fw = open('cam2.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
			if self.screen4_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene4.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene4.mayavi_scene)
				
				fw = open('cam2.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
		
		# Update camera values
		self.updateCurrentVals_button_fired()
	
	@on_trait_change('saveCam3')
	def saveCam3_fired(self):
		
		# Save and load camera state
		
		if os.path.isfile('cam3.txt'):
			
			if self.screen1_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam3.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene1.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene1.mayavi_scene)
			
			if self.screen2_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam3.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene2.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene2.mayavi_scene)
			
			if self.screen3_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam3.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene3.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene3.mayavi_scene)
			
			if self.screen4_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam3.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene4.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene4.mayavi_scene)
		
		else:
		
			# Get current cam values for active screen
			# NOTE: Only one screen can be active at a time
			if self.screen1_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene1.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene1.mayavi_scene)
				
				fw = open('cam3.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
			if self.screen2_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene2.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene2.mayavi_scene)
				
				fw = open('cam3.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
			if self.screen3_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene3.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene3.mayavi_scene)
				
				fw = open('cam3.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
			if self.screen4_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene4.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene4.mayavi_scene)
				
				fw = open('cam3.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
		
		# Update camera values
		self.updateCurrentVals_button_fired()
	
	@on_trait_change('saveCam4')
	def saveCam4_fired(self):
		
		# Save and load camera state
		
		if os.path.isfile('cam4.txt'):
			
			if self.screen1_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam4.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene1.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene1.mayavi_scene)
			
			if self.screen2_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam4.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene2.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene2.mayavi_scene)
			
			if self.screen3_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam4.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene3.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene3.mayavi_scene)
			
			if self.screen4_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam4.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene4.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene4.mayavi_scene)
		
		else:
		
			# Get current cam values for active screen
			# NOTE: Only one screen can be active at a time
			if self.screen1_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene1.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene1.mayavi_scene)
				
				fw = open('cam4.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
			if self.screen2_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene2.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene2.mayavi_scene)
				
				fw = open('cam4.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
			if self.screen3_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene3.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene3.mayavi_scene)
				
				fw = open('cam4.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
			if self.screen4_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene4.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene4.mayavi_scene)
				
				fw = open('cam4.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
		
		# Update camera values
		self.updateCurrentVals_button_fired()
	
	@on_trait_change('saveCam5')
	def saveCam5_fired(self):
		
		# Save and load camera state
		
		if os.path.isfile('cam5.txt'):
			
			if self.screen1_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam5.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene1.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene1.mayavi_scene)
			
			if self.screen2_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam5.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene2.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene2.mayavi_scene)
			
			if self.screen3_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam5.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene3.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene3.mayavi_scene)
			
			if self.screen4_ts1:
				camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll = np.loadtxt('cam5.txt')
				
				mlab.view(camAzimuth, camElevation, camDistance, [fp1, fp2, fp3], figure=self.scene4.mayavi_scene)
				mlab.roll(camRoll, figure=self.scene4.mayavi_scene)
		
		else:
		
			# Get current cam values for active screen
			# NOTE: Only one screen can be active at a time
			if self.screen1_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene1.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene1.mayavi_scene)
				
				fw = open('cam5.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
			if self.screen2_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene2.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene2.mayavi_scene)
				
				fw = open('cam5.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
			if self.screen3_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene3.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene3.mayavi_scene)
				
				fw = open('cam5.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
			if self.screen4_ts1:
				camAzimuth, camElevation, camDistance, fp = mlab.view(figure=self.scene4.mayavi_scene)	
				fp1, fp2, fp3 = fp
				camRoll = mlab.roll(figure=self.scene4.mayavi_scene)
				
				fw = open('cam5.txt', 'w+')
				fw.write(str(np.float32(camAzimuth)) + ' ' + \
						str(np.float32(camElevation)) + ' ' + \
						str(np.float32(camDistance)) + ' ' + \
						str(np.float32(fp1)) + ' ' + \
						str(np.float32(fp2)) + ' ' + \
						str(np.float32(fp3)) + ' ' + \
						str(np.float32(camRoll)) + ' ' 
						)
				
				fw.close()
		
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
		if self.screen1_ts1:
			mlab.view(self.camAzimuthS, self.camElevationS, self.camDistanceS, [self.focalPointS1, self.focalPointS2, self.focalPointS3], figure=self.scene1.mayavi_scene)
			mlab.roll(self.camRollS, figure=self.scene1.mayavi_scene)
		
		# Update camera view for screen 2
		if self.screen2_ts1:
			mlab.view(self.camAzimuthS, self.camElevationS, self.camDistanceS, [self.focalPointS1, self.focalPointS2, self.focalPointS3], figure=self.scene2.mayavi_scene)
			mlab.roll(self.camRollS, figure=self.scene2.mayavi_scene)
		
		# Update camera view for screen 3
		if self.screen3_ts1:
			mlab.view(self.camAzimuthS, self.camElevationS, self.camDistanceS, [self.focalPointS1, self.focalPointS2, self.focalPointS3], figure=self.scene3.mayavi_scene)
			mlab.roll(self.camRollS, figure=self.scene3.mayavi_scene)
		
		# Update camera view for screen 4
		if self.screen4_ts1:
			mlab.view(self.camAzimuthS, self.camElevationS, self.camDistanceS, [self.focalPointS1, self.focalPointS2, self.focalPointS3], figure=self.scene4.mayavi_scene)
			mlab.roll(self.camRollS, figure=self.scene4.mayavi_scene)
		
